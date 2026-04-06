# Use Case: Bình Luận Sản Phẩm

## Thông Tin Chung

| Thuộc tính | Mô tả |
|------------|-------|
| **Use Case ID** | UC-003 |
| **Use Case Name** | Bình Luận Sản Phẩm (Product Comment) |
| **Actor** | Người dùng đã đăng nhập, Admin, Manager |
| **Description** | Cho phép người dùng đăng bình luận, đặt câu hỏi hoặc chia sẻ ý kiến về sản phẩm. Hệ thống tích hợp **AI phân tích cảm xúc (Sentiment Analysis)** để tự động đánh giá nội dung bình luận, xác định các khía cạnh (aspect) và cảm xúc (positive/negative/neutral). |

---

## Điều Kiện

| Loại | Mô tả |
|------|-------|
| **Preconditions** | 1. Người dùng đã đăng nhập vào hệ thống<br>2. Sản phẩm tồn tại và đang hoạt động<br>3. Dịch vụ AI phân tích (ML Service) khả dụng (không bắt buộc) |
| **Postconditions** | 1. Bình luận được lưu vào database<br>2. AI phân tích cảm xúc và lưu kết quả (nếu thành công)<br>3. Bình luận hiển thị trên trang sản phẩm với badge cảm xúc |
| **Trigger** | Người dùng nhấn nút "Đăng bình luận" hoặc "Trả lời" trên trang chi tiết sản phẩm |

---

## Luồng Xử Lý

### Normal Flow (Luồng Chính) - Đăng Bình Luận Mới

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Truy cập trang chi tiết sản phẩm | Hiển thị thông tin sản phẩm và section bình luận |
| 2 | - | Load danh sách bình luận (10 comments/trang, sắp xếp mới nhất) |
| 3 | Nhập nội dung bình luận (1-1000 ký tự) | - |
| 4 | Nhấn nút "Đăng bình luận" | - |
| 5 | - | Validate nội dung (frontend) |
| 6 | - | Gửi request POST /api/comments |
| 7 | - | Backend validate dữ liệu |
| 8 | - | **Gọi AI Service phân tích cảm xúc** |
| 9 | - | AI trả về kết quả: aspects, sentiment, confidence |
| 10 | - | Lưu comment + aiAnalysis vào database |
| 11 | - | Trả về comment với thông tin AI analysis |
| 12 | - | Hiển thị toast "Đã đăng bình luận thành công!" |
| 13 | - | Refresh danh sách bình luận |
| 14 | - | Hiển thị bình luận mới với **badge cảm xúc** |

---

### AI Sentiment Analysis Flow (Chi Tiết Phân Tích AI)

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI ANALYSIS PIPELINE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Input: "Sản phẩm chất lượng tốt, giao hàng nhanh, giá hơi cao" │
│                           ↓                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  ML Service (https://api.honeysocial.click/predict)     │    │
│  │  - Aspect-Based Sentiment Analysis                       │    │
│  │  - Natural Language Processing                           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           ↓                                      │
│  Output:                                                         │
│  {                                                               │
│    "results": [                                                  │
│      { "aspect": "chất lượng", "sentiment": "positive", "confidence": 0.92 },
│      { "aspect": "giao hàng", "sentiment": "positive", "confidence": 0.88 },
│      { "aspect": "giá", "sentiment": "negative", "confidence": 0.75 }
│    ]                                                             │
│  }                                                               │
│                           ↓                                      │
│  Display: [chất lượng POSITIVE] [giao hàng POSITIVE] [giá NEGATIVE]
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Sentiment Badge Colors

| Sentiment | Color | CSS Class |
|-----------|-------|-----------|
| **positive** | Xanh lá | `bg-green-100 text-green-800 border-green-200` |
| **negative** | Đỏ | `bg-red-100 text-red-800 border-red-200` |
| **neutral** | Xám | `bg-gray-100 text-gray-800 border-gray-200` |

---

### Alternative Flows (Luồng Thay Thế)

#### AF-1: Trả Lời Bình Luận (Reply)
| Bước | Mô tả |
|------|-------|
| 1 | Người dùng nhấn "Trả lời" trên một bình luận |
| 2 | Hiển thị form trả lời inline |
| 3 | Người dùng nhập nội dung trả lời |
| 4 | Nhấn "Đăng trả lời" |
| 5 | Gửi request với `parentId` = ID bình luận cha |
| 6 | **Lưu ý: Reply không có AI analysis** (chỉ root comments) |
| 7 | Hiển thị reply lồng dưới bình luận cha |

#### AF-2: AI Service Không Khả Dụng
| Bước | Mô tả |
|------|-------|
| 1 | Gọi AI Service thất bại (timeout, error) |
| 2 | Log warning nhưng không fail việc tạo comment |
| 3 | Lưu comment với `aiAnalysis = null` |
| 4 | Bình luận hiển thị bình thường (không có badge cảm xúc) |

#### AF-3: Xem Thêm Bình Luận
| Bước | Mô tả |
|------|-------|
| 1 | Người dùng nhấn "Xem thêm bình luận" |
| 2 | Load trang tiếp theo (page + 1) |
| 3 | Append bình luận mới vào danh sách |

#### AF-4: Chỉnh Sửa Bình Luận (Chủ sở hữu)
| Bước | Mô tả |
|------|-------|
| 1 | Chủ sở hữu nhấn "Sửa" trên bình luận của mình |
| 2 | Chuyển sang chế độ edit |
| 3 | Sửa nội dung |
| 4 | Gửi PUT /api/comments/:id |
| 5 | Cập nhật bình luận (không re-analyze AI) |

#### AF-5: Xóa Bình Luận
| Bước | Mô tả |
|------|-------|
| 1 | Chủ sở hữu hoặc Admin/Manager nhấn "Xóa" |
| 2 | Hiển thị confirm dialog |
| 3 | Gửi DELETE /api/comments/:id |
| 4 | Xóa comment + tất cả replies (cascade) |
| 5 | Hiển thị toast "Đã xóa bình luận thành công" |

---

### Exception Flows (Luồng Ngoại Lệ)

#### EX-1: Chưa Đăng Nhập
| Bước | Mô tả |
|------|-------|
| Điều kiện | Người dùng chưa đăng nhập |
| Xử lý | Lưu redirectPath, chuyển hướng đến /login |
| Kết quả | Sau đăng nhập, quay lại trang sản phẩm |

#### EX-2: Nội Dung Rỗng
| Bước | Mô tả |
|------|-------|
| Điều kiện | Nội dung bình luận trống hoặc chỉ có khoảng trắng |
| Xử lý | Hiển thị lỗi "Nội dung bình luận không được để trống" |
| Kết quả | Người dùng nhập nội dung |

#### EX-3: Nội Dung Quá Dài
| Bước | Mô tả |
|------|-------|
| Điều kiện | Nội dung vượt quá 1000 ký tự |
| Xử lý | Hiển thị lỗi "Nội dung bình luận không được vượt quá 1000 ký tự" |
| Kết quả | Người dùng rút ngắn nội dung |

#### EX-4: Sản Phẩm Không Tồn Tại
| Bước | Mô tả |
|------|-------|
| Điều kiện | productId không hợp lệ |
| Xử lý | Trả về lỗi "Không tìm thấy sản phẩm" |
| Kết quả | Người dùng quay lại trang sản phẩm hợp lệ |

#### EX-5: Bình Luận Cha Không Tồn Tại (Reply)
| Bước | Mô tả |
|------|-------|
| Điều kiện | parentId không hợp lệ khi reply |
| Xử lý | Trả về lỗi "Không tìm thấy bình luận cha" |
| Kết quả | Refresh trang để cập nhật danh sách |

#### EX-6: Không Có Quyền Sửa/Xóa
| Bước | Mô tả |
|------|-------|
| Điều kiện | Người dùng không phải chủ sở hữu và không phải Admin/Manager |
| Xử lý | Trả về lỗi "Bạn không có quyền chỉnh sửa bình luận này" |
| Kết quả | Từ chối thao tác |

---

## Business Rules

| Rule ID | Mô tả |
|---------|-------|
| BR-001 | Chỉ người dùng đã đăng nhập mới được bình luận |
| BR-002 | Nội dung bình luận từ 1-1000 ký tự |
| BR-003 | Chủ sở hữu có thể sửa/xóa bình luận của mình |
| BR-004 | Admin/Manager có thể xóa bất kỳ bình luận nào |
| BR-005 | Xóa bình luận cha sẽ cascade xóa tất cả replies |
| BR-006 | **AI Analysis chỉ áp dụng cho root comments, không áp dụng cho replies** |
| BR-007 | AI Service failure không block việc tạo comment |
| BR-008 | Pagination: 10 root comments per page |
| BR-009 | Default sort: newest first |

---

## AI Analysis Details

### Request to ML Service
```json
POST https://api.honeysocial.click/predict
{
  "text": "Nội dung bình luận của người dùng"
}
```

### Response from ML Service
```json
{
  "results": [
    {
      "aspect": "chất lượng",
      "sentiment": "positive",
      "confidence": 0.92
    },
    {
      "aspect": "giao hàng", 
      "sentiment": "positive",
      "confidence": 0.88
    },
    {
      "aspect": "giá cả",
      "sentiment": "negative", 
      "confidence": 0.75
    }
  ]
}
```

### Stored aiAnalysis Field
```json
{
  "results": [
    { "aspect": "...", "sentiment": "positive|negative|neutral", "confidence": 0.0-1.0 }
  ]
}
```

---

## UI Elements

| Element | Loại | Mô tả |
|---------|------|-------|
| Comment Form | Textarea | Nhập nội dung (max 1000 chars) |
| Đăng bình luận | Button | Submit form |
| Comment Item | Component | Hiển thị avatar, tên, thời gian, nội dung, badges |
| Sentiment Badges | Tags | Hiển thị aspect + sentiment với màu tương ứng |
| Trả lời | Button | Mở form reply inline |
| Xóa | Button | Xóa comment (owner/admin only) |
| Xem thêm | Button | Load more comments |
| Loading Spinner | Animation | Hiển thị khi đang load |

---

## API Endpoints

| Method | Endpoint | Auth | Request | Response |
|--------|----------|------|---------|----------|
| GET | `/api/comments?productId=&page=&limit=&sortBy=` | No | Query params | `{ comments[], pagination }` |
| GET | `/api/comments/:id` | No | - | `{ comment with replies }` |
| POST | `/api/comments` | Yes | `{ productId, content, parentId? }` | `{ comment with aiAnalysis }` |
| PUT | `/api/comments/:id` | Yes (owner/admin) | `{ content }` | `{ updated comment }` |
| DELETE | `/api/comments/:id` | Yes (owner/admin) | - | `{ success }` |

---

## Data Model

### Comment Entity
```typescript
interface Comment {
  id: string;
  productId: string;
  userId: string;
  content: string;
  parentId?: string;        // null for root comments
  aiAnalysis?: {            // AI sentiment analysis result
    results: Array<{
      aspect: string;
      sentiment: 'positive' | 'negative' | 'neutral';
      confidence: number;   // 0.0 - 1.0
    }>;
  };
  createdAt: Date;
  updatedAt: Date;
  
  // Relations
  user: { id, name, avatar, role };
  replies?: Comment[];      // Nested replies
}
```

---

## Sequence Diagram Reference

```
User → Product Page → Comment Form → Validate → API Create Comment
  → Backend Validate → AI Service (async) → Parse Aspects & Sentiments
  → Save Comment + AI Analysis → Return Response → Display with Badges
```

---

## Use Cases Liên Quan

| UC ID | Tên | Mô tả |
|-------|-----|-------|
| UC-002 | Đăng Nhập | Yêu cầu đăng nhập trước khi bình luận |
| UC-004 | Xem Chi Tiết Sản Phẩm | Hiển thị section bình luận |
| UC-005 | Đánh Giá Sản Phẩm (Review) | Khác với comment, review có rating stars |
