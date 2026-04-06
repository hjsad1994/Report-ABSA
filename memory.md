# Vietnamese ABSA Project Memory

## Tổng Quan Dự Án

Dự án phân tích cảm xúc dựa trên khía cạnh (Aspect-Based Sentiment Analysis - ABSA) cho tiếng Việt, với 2 nhiệm vụ chính:
- **Aspect Detection (AD)**: Xác định 11 khía cạnh (Battery, Camera, Performance, Display, Design, Packaging, Price, Shop_Service, Shipping, General, Others)
- **Sentiment Classification (SC)**: Phân loại cảm xúc 3 lớp (Positive/Negative/Neutral) cho 10 khía cạnh (trừ Others)

---

## Các Mô Hình Đã Phát Triển

### 1. BILSTM-based Models (Traditional Deep Learning)

| Mô Hình | Kiến Trúc | AD F1 | SC F1 |
|---------|-----------|-------|-------|
| **BILSTM-MTL** | BiLSTM + Conv1D + MTL | 84.09% | 33.48% |
| **BILSTM-MTL-NoCon** | BiLSTM + MTL (không Conv1D) | 82.85% | 34.28% |
| **BILSTM-STL** | BiLSTM + Conv1D + STL | 86.23% | 36.87% |
| **BILSTM-STL-NoCon** | BiLSTM + STL | 85.69% | 39.83% |

**Đặc điểm:**
- Sử dụng FastText embeddings (300D)
- Transfer Learning ở mức embeddings
- AD performance tốt (~82-86%), SC performance thấp (~27-40%)

### 2. PhoBERT-based Models (Pretrained Vietnamese BERT)

| Mô Hình | Kiến Trúc | AD F1 | SC F1 |
|---------|-----------|-------|-------|
| **phoBERT-MTL** | vinai/phobert-base + MTL | 66.28% | 92.93% |
| **PhoBERT-STL** | vinai/phobert-base + STL | 88.84% | 92.06% |

**Đặc điểm:**
- Fine-tuning pretrained phoBERT (135M parameters)
- SC performance xuất sắc (~92%)
- MTL có AD thấp, STL cải thiện AD +22.56%

### 3. VisoBERT-based Models (Best Performance)

| Mô Hình | Kiến Trúc | AD F1 | SC F1 |
|---------|-----------|-------|-------|
| **VisoBERT-MTL** | 5CD-AI/visobert-14gb-corpus + MTL | 82.68% | 93.63% |
| **VisoBERT-STL** | 5CD-AI/visobert-14gb-corpus + STL | **89.39%** | **96.37%** |

**Đặc điểm:**
- VisoBERT được train trên corpus 14GB tiếng Việt
- **VisoBERT-STL đạt performance cao nhất** cả 2 tasks

---

## Bảng So Sánh Tổng Hợp

| Mô Hình | AD F1 | AD Precision | AD Recall | SC F1 | SC Precision | SC Recall |
|---------|-------|--------------|-----------|-------|--------------|-----------|
| BILSTM-MTL | 84.09% | 78.91% | 90.59% | 33.48% | 43.90% | 67.03% |
| BILSTM-MTL-NoCon | 82.85% | 77.83% | 88.73% | 34.28% | 48.97% | 69.60% |
| BILSTM-STL | 86.23% | 83.56% | 89.50% | 36.87% | 38.45% | 68.07% |
| BILSTM-STL-NoCon | 85.69% | 81.94% | 90.59% | 39.83% | 39.00% | 70.78% |
| phoBERT-MTL | 66.28% | 56.27% | 86.16% | 92.93% | 92.34% | 93.81% |
| PhoBERT-STL | 88.84% | 85.50% | 92.88% | 92.06% | 92.25% | 92.27% |
| VisoBERT-MTL | 82.68% | 73.83% | 90.39% | 93.63% | 94.01% | 93.56% |
| **VisoBERT-STL** | **89.39%** | **86.77%** | 92.36% | **96.37%** | **96.37%** | 95.44% |

---

## Kỹ Thuật Đã Áp Dụng

### 1. Learning Approaches
- **Multi-Task Learning (MTL)**: Train AD và SC đồng thời với shared backbone
- **Single-Task Learning (STL)**: Train AD và SC riêng biệt, mỗi task có mô hình độc lập

### 2. Loss Functions
- **Focal Loss**: Xử lý class imbalance cho cả AD và SC
- **Binary Focal Loss**: Cho AD (multi-label binary classification)
- **Multi-class Focal Loss**: Cho SC (3-class per aspect)

### 3. Model Architectures
- **BiLSTM + Conv1D**: Capture sequential và local patterns
- **Transformer (BERT)**: Self-attention cho contextualized representations
- **Task Heads**: Separate classification heads cho AD và SC

### 4. Transfer Learning vs Fine-Tuning
- **BILSTM**: Transfer Learning (chỉ pretrained embeddings)
- **phoBERT/VisoBERT**: Full Fine-Tuning (toàn bộ pretrained model)

---

## Kết Luận và Phát Hiện Quan Trọng

### 1. STL > MTL cho task này
- PhoBERT-STL: AD +22.56% so với phoBERT-MTL
- VisoBERT-STL: AD +6.71%, SC +2.74% so với VisoBERT-MTL
- Riêng biệt training giúp mỗi task được tối ưu riêng, không bị task interference

### 2. Transformer > BiLSTM
- SC: 96.37% (VisoBERT) vs 39.83% (BILSTM) = +56.54%
- Pretrained transformers có contextualized representations mạnh hơn

### 3. VisoBERT > phoBERT
- VisoBERT-STL: AD 89.39%, SC 96.37%
- PhoBERT-STL: AD 88.84%, SC 92.06%
- VisoBERT được train trên corpus lớn hơn (14GB) cho kết quả tốt hơn

### 4. Mô Hình Khuyến Nghị
- **Production**: VisoBERT-STL (best performance)
- **Alternative**: PhoBERT-STL (nhẹ hơn, performance tốt)
- **Baseline**: BILSTM-MTL (cho comparison với traditional methods)

---

## Cấu Trúc Thư Mục

```
E:\BERT\
├── BILSTM-MTL/          # BiLSTM Multi-Task Learning with Conv1D
├── BILSTM-MTL-NoCon/    # BiLSTM MTL without Conv1D
├── BILSTM-STL/          # BiLSTM Single-Task Learning with Conv1D
├── BILSTM-STL-NoCon/    # BiLSTM STL without Conv1D
├── phoBERT-MTL/         # phoBERT Multi-Task Learning
├── PhoBERT-STL/         # phoBERT Single-Task Learning
├── VisoBERT-MTL/        # VisoBERT Multi-Task Learning
├── VisoBERT-STL/        # VisoBERT Single-Task Learning (BEST)
├── dataset/             # Dataset files
├── dataset.csv          # Main dataset
└── requirements.txt     # Project dependencies
```

---

## Các File Quan Trọng

### Mỗi Model Folder chứa:
- `config_*.yaml` - Cấu hình training
- `train_*.py` - Script training
- `model_*.py` - Model architecture
- `dataset_*.py` - Data loading
- `models/` - Saved models và results
  - `best_model.pt` - Best checkpoint
  - `test_results.json` - Evaluation metrics
  - `training_history.csv` - Training logs
  - `final_report.txt` - Summary report

---

## Ngày Cập Nhật
- **Tạo**: 2025-12-06
- **Phiên bản**: 1.0
