# =============================================================================
# Replication v2 — เป้าหมาย: ตัวเลขใกล้เคียง Paper มากที่สุด
#   "A credit card fraud detection approach based on ensemble machine
#    learning classifier with hybrid data sampling"
#   Ahmed et al., Machine Learning with Applications 20 (2025) 100675
#
# *** การเปลี่ยนแปลงจาก v1 ***
# จากการ reverse-engineer ขนาด test set ใน confusion matrix ของ Paper:
#   - Table 1 (No-sampling)    : test ≈ 55,133  (≈19.4% ของ data หลัง drop-dup)
#   - Table 4 (Under-Sampling) : test ≈ 190     -> Paper undersample "ก่อน" split
#   - Table 7 (SMOTE)          : test ≈ 110,076 -> Paper SMOTE "ก่อน" split
#   - Table 10 (SMOTE+ENN)     : test ≈ 82,472  -> Paper SMOTE+ENN "ก่อน" split
# ดังนั้นโค้ดนี้จึงทำ resample "ก่อน" แบ่ง train/test (ตามที่ Paper ทำจริง)
# แม้จะมี data leakage แต่นี่คือ methodology ที่ Paper ใช้
# =============================================================================

# ---- Mount Google Drive (สำหรับ Google Colab) ----
from google.colab import drive
drive.mount('/content/drive')

import os
import warnings
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
)

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler, EditedNearestNeighbours
from imblearn.combine import SMOTEENN

warnings.filterwarnings("ignore")

RANDOM_STATE = 42
TEST_SIZE    = 0.20
DATA_PATH    = "/content/drive/MyDrive/Dataset.csv"   # <-- แก้ path ตรงนี้แล้ว
OUT_DIR      = "outputs_v2"
os.makedirs(OUT_DIR, exist_ok=True)


# ----- Section 3.5.1: Pre-processing -----
def load_and_preprocess(path: str):
    df = pd.read_csv(path)
    print(f"[Load] shape: {df.shape}")
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"[Preprocess] removed {before - len(df)} duplicates -> {len(df)}")

    scaler = StandardScaler()
    df["Amount"] = scaler.fit_transform(df[["Amount"]])
    df = df.drop(columns=["Time"])
    return df


def build_models():
    """Section 4: KNN(5), RF(100), AdaBoost(50), Voting='soft'"""
    base_estimators = [
        ("ada", AdaBoostClassifier(n_estimators=50, random_state=RANDOM_STATE)),
        ("rf",  RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1)),
        ("knn", KNeighborsClassifier(n_neighbors=5)),
    ]
    return {
        "AdaBoost": AdaBoostClassifier(n_estimators=50, random_state=RANDOM_STATE),
        "RF":       RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1),
        "KNN":      KNeighborsClassifier(n_neighbors=5),
        "Proposed": VotingClassifier(estimators=base_estimators, voting="soft", n_jobs=-1),
    }


def evaluate(name, model, X_tr, y_tr, X_te, y_te):
    model.fit(X_tr, y_tr)
    y_pred = model.predict(X_te)
    tn, fp, fn, tp = confusion_matrix(y_te, y_pred).ravel()
    return {
        "Model": name,
        "TP": int(tp), "TN": int(tn), "FP": int(fp), "FN": int(fn),
        "Accuracy":  round(accuracy_score(y_te, y_pred), 5),
        "Precision": round(precision_score(y_te, y_pred, zero_division=0), 3),
        "Recall":    round(recall_score(y_te, y_pred, zero_division=0), 3),
        "F1":        round(f1_score(y_te, y_pred, zero_division=0), 3),
    }


def run_scenario(name, X_data, y_data):
    """แบ่ง train/test 80/20 บนข้อมูลที่ให้มา แล้ว fit-evaluate ทุกโมเดล"""
    print(f"\n========== {name} ==========")
    X_tr, X_te, y_tr, y_te = train_test_split(
        X_data, y_data, test_size=TEST_SIZE,
        random_state=RANDOM_STATE, stratify=y_data, shuffle=True
    )
    print(f"  train: {X_tr.shape}, test: {X_te.shape}")
    print(f"  test class counts: {dict(zip(*np.unique(y_te, return_counts=True)))}")

    rows = []
    for m_name, model in build_models().items():
        print(f"  ... {m_name}")
        rows.append(evaluate(m_name, model, X_tr, y_tr, X_te, y_te))
        r = rows[-1]
        print(f"     TP={r['TP']} TN={r['TN']} FP={r['FP']} FN={r['FN']} "
              f"Acc={r['Accuracy']} P={r['Precision']} R={r['Recall']} F1={r['F1']}")
    return rows


# ============== MAIN ==============
df = load_and_preprocess(DATA_PATH)
X = df.drop(columns=["Class"]).values
y = df["Class"].values

all_results = {}

# ----- 4.1: Without Sampling -----
all_results["no_sampling"] = run_scenario("Without Sampling (4.1)", X, y)

# ----- 4.2: Under-Sampling (ทำก่อนแบ่ง train/test เพื่อให้ test size = 190 ตรง Paper) -----
rus = RandomUnderSampler(sampling_strategy="auto", random_state=RANDOM_STATE)
X_us, y_us = rus.fit_resample(X, y)
print(f"\n[Under-Sample] full data after undersample: {X_us.shape}, "
      f"counts: {dict(zip(*np.unique(y_us, return_counts=True)))}")
all_results["under"] = run_scenario("Under-Sampling (4.2)", X_us, y_us)

# ----- 4.3: SMOTE (ก่อนแบ่ง train/test เพื่อให้ test ≈ 110k ตรง Paper) -----
sm = SMOTE(sampling_strategy="auto", random_state=RANDOM_STATE)
X_sm, y_sm = sm.fit_resample(X, y)
print(f"\n[SMOTE] full data after SMOTE: {X_sm.shape}, "
      f"counts: {dict(zip(*np.unique(y_sm, return_counts=True)))}")
all_results["smote"] = run_scenario("SMOTE (4.3)", X_sm, y_sm)

# ----- 4.4: SMOTE+ENN (sampling_strategy=0.5 ตามที่ Paper ระบุในหน้า 7) -----
smen = SMOTEENN(
    smote=SMOTE(sampling_strategy=0.5, random_state=RANDOM_STATE),
    enn=EditedNearestNeighbours(),
    random_state=RANDOM_STATE,
)
X_se, y_se = smen.fit_resample(X, y)
print(f"\n[SMOTE+ENN] full data after SMOTE+ENN: {X_se.shape}, "
      f"counts: {dict(zip(*np.unique(y_se, return_counts=True)))}")
all_results["smoteenn"] = run_scenario("SMOTE + ENN (4.4)", X_se, y_se)


# ============== Export Tables 1-13 ==============
def fmt_table(rows, metric_cols):
    df = pd.DataFrame(rows).set_index("Model")
    return df[metric_cols]


with open(os.path.join(OUT_DIR, "tables_all.md"), "w", encoding="utf-8") as f:
    f.write("# Replication Results — Tables 1-13\n\n")

    def w_table(title, rows, cols, transpose=False):
        f.write(f"\n## {title}\n\n")
        df = pd.DataFrame(rows).set_index("Model")[cols]
        if transpose:
            df = df.T
        f.write(df.to_markdown())
        f.write("\n")
        print(f"\n--- {title} ---")
        print(df.to_string())

    # ----- Tables 1, 2, 3 -----
    w_table("Table 1: Confusion matrix (Without Sampling)",
            all_results["no_sampling"], ["TP", "TN", "FP", "FN"], transpose=True)
    w_table("Table 2: Accuracy (Without Sampling)",
            all_results["no_sampling"], ["Accuracy"], transpose=True)
    w_table("Table 3: Precision/Recall/F1 (Without Sampling)",
            all_results["no_sampling"], ["Precision", "Recall", "F1"], transpose=True)

    # ----- Tables 4, 5, 6 -----
    w_table("Table 4: Confusion matrix (Under-Sampling)",
            all_results["under"], ["TP", "TN", "FP", "FN"], transpose=True)
    w_table("Table 5: Accuracy (Under-Sampling)",
            all_results["under"], ["Accuracy"], transpose=True)
    w_table("Table 6: Precision/Recall/F1 (Under-Sampling)",
            all_results["under"], ["Precision", "Recall", "F1"], transpose=True)

    # ----- Tables 7, 8, 9 -----
    w_table("Table 7: Confusion matrix (SMOTE)",
            all_results["smote"], ["TP", "TN", "FP", "FN"], transpose=True)
    w_table("Table 8: Accuracy (SMOTE)",
            all_results["smote"], ["Accuracy"], transpose=True)
    w_table("Table 9: Precision/Recall/F1 (SMOTE)",
            all_results["smote"], ["Precision", "Recall", "F1"], transpose=True)

    # ----- Tables 10, 11, 12 -----
    w_table("Table 10: Confusion matrix (SMOTE + ENN)",
            all_results["smoteenn"], ["TP", "TN", "FP", "FN"], transpose=True)
    w_table("Table 11: Accuracy (SMOTE + ENN)",
            all_results["smoteenn"], ["Accuracy"], transpose=True)
    w_table("Table 12: Precision/Recall/F1 (SMOTE + ENN)",
            all_results["smoteenn"], ["Precision", "Recall", "F1"], transpose=True)

    # ----- Table 13: Comparison with prior work -----
    proposed = next(r for r in all_results["smoteenn"] if r["Model"] == "Proposed")
    table13 = pd.DataFrame({
        "Sahithi et al. (2022)":  [0.99945, 0.99947, 0.99945, 0.99946],
        "Prusti & Rath (2019)":   [0.8383,  0.945,   0.8647,  0.9031 ],
        "Khalid et al. (2024)":   [0.99959, 0.9996,  0.9996,  0.9996 ],
        "Proposed (SMOTE+ENN)":   [proposed["Accuracy"], proposed["Precision"],
                                   proposed["Recall"],   proposed["F1"]],
    }, index=["Accuracy", "Precision", "Recall", "F1"])
    f.write("\n## Table 13: Comparison with existing models\n\n")
    f.write(table13.to_markdown())
    f.write("\n")
    print("\n--- Table 13 ---")
    print(table13.to_string())

    # Save raw CSV for all
    pd.DataFrame([r for rows in all_results.values() for r in rows]).to_csv(
        os.path.join(OUT_DIR, "raw_all_results.csv"), index=False
    )

print(f"\nเสร็จ — ดูผลที่ {OUT_DIR}/tables_all.md")
