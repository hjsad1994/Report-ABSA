# Hiện Thực Hệ Thống

## Tổng Quan Kiến Trúc

VeritaShop được xây dựng theo kiến trúc **Client-Server** với 3 thành phần chính:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           VERITASHOP ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌──────────────┐      ┌──────────────┐      ┌──────────────────┐      │
│   │   Frontend   │ ──── │   Backend    │ ──── │    Database      │      │
│   │   (Next.js)  │ HTTP │  (Express)   │      │   (PostgreSQL)   │      │
│   │   Port 5000  │ API  │  Port 3001   │      │    Port 5436     │      │
│   └──────────────┘      └──────┬───────┘      └──────────────────┘      │
│                                │                                         │
│                                │ HTTP                                    │
│                                ▼                                         │
│                      ┌──────────────────┐                               │
│                      │   ML Service     │                               │
│                      │  (Sentiment AI)  │                               │
│                      │   NLP Module     │                               │
│                      └──────────────────┘                               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Application UI (Frontend)

### Công Nghệ Sử Dụng

| Công nghệ | Phiên bản | Mô tả |
|-----------|-----------|-------|
| **Next.js** | 15.0.3 | React Framework với App Router, Server Components |
| **React** | 19.0.0 | UI Library |
| **TypeScript** | 5.x | Type-safe JavaScript |
| **Tailwind CSS** | 3.4.1 | Utility-first CSS Framework |
| **Axios** | 1.13.2 | HTTP Client |
| **react-hot-toast** | 2.6.0 | Toast notifications |

### Cấu Trúc Thư Mục

```
frontend/src/
├── app/                    # Next.js App Router (Pages)
│   ├── admin/              # Trang quản trị
│   ├── shop/               # Trang cửa hàng
│   ├── checkout/           # Thanh toán
│   ├── login/              # Đăng nhập
│   ├── register/           # Đăng ký
│   ├── profile/            # Hồ sơ người dùng
│   ├── orders/             # Đơn hàng
│   ├── category/           # Danh mục sản phẩm
│   ├── payment/            # Thanh toán
│   └── layout.tsx          # Root layout
│
├── components/             # Shared Components
│   ├── admin/              # Admin components
│   ├── auth/               # Authentication components
│   ├── layout/             # Header, Footer, Sidebar
│   └── ui/                 # UI primitives (Button, Input, Modal...)
│
├── features/               # Feature-based modules
│   ├── admin/              # Admin dashboard features
│   ├── checkout/           # Checkout flow
│   ├── home/               # Homepage features
│   └── shop/               # Shop & Product features
│       └── components/
│           └── comments/   # Comment system with AI badges
│
├── contexts/               # React Contexts
│   └── AuthContext.tsx     # Authentication state
│
├── lib/                    # Utilities & Services
│   ├── api/                # API service layer
│   │   ├── authService.ts
│   │   ├── productService.ts
│   │   ├── commentService.ts
│   │   └── types.ts
│   └── data/               # Static data
│
├── styles/                 # Global styles
└── middleware.ts           # Next.js middleware (auth protection)
```

### Các Trang Chính

| Trang | Route | Mô tả |
|-------|-------|-------|
| Trang chủ | `/` | Sản phẩm nổi bật, danh mục |
| Cửa hàng | `/shop` | Danh sách sản phẩm, filter, search |
| Chi tiết SP | `/shop/[slug]` | Thông tin SP, bình luận, đánh giá |
| Danh mục | `/category/[slug]` | Sản phẩm theo danh mục |
| Giỏ hàng | `/checkout` | Quản lý giỏ hàng |
| Thanh toán | `/payment` | Xử lý thanh toán |
| Đăng nhập | `/login` | Xác thực người dùng |
| Đăng ký | `/register` | Tạo tài khoản mới |
| Hồ sơ | `/profile` | Thông tin cá nhân |
| Đơn hàng | `/orders` | Lịch sử đơn hàng |
| Admin | `/admin/*` | Quản trị hệ thống |

### Component Bình Luận với AI

```typescript
// CommentItem.tsx - Hiển thị badge sentiment
{comment.aiAnalysis?.results?.map((analysis, idx) => (
  <span 
    key={idx} 
    className={`text-xs px-2 py-0.5 rounded-full border ${getSentimentColor(analysis.sentiment)}`}
    title={`Confidence: ${(analysis.confidence * 100).toFixed(1)}%`}
  >
    <span className="font-medium">{analysis.aspect}</span>
    <span className="opacity-75 text-[10px] uppercase">{analysis.sentiment}</span>
  </span>
))}

// Sentiment colors
const getSentimentColor = (sentiment: string) => {
  switch (sentiment) {
    case 'positive': return 'bg-green-100 text-green-800 border-green-200';
    case 'negative': return 'bg-red-100 text-red-800 border-red-200';
    default: return 'bg-gray-100 text-gray-800 border-gray-200';
  }
};
```

---

## Backend

### Công Nghệ Sử Dụng

| Công nghệ | Phiên bản | Mô tả |
|-----------|-----------|-------|
| **Node.js** | 18+ | Runtime environment |
| **Express** | 4.21.2 | Web framework |
| **TypeScript** | 5.7.3 | Type-safe JavaScript |
| **Prisma** | 5.15.0 | ORM (Object-Relational Mapping) |
| **PostgreSQL** | 13 | Relational database |
| **JWT** | 9.0.2 | JSON Web Token authentication |
| **bcryptjs** | 2.4.3 | Password hashing |
| **Cloudinary** | 2.5.1 | Image hosting |
| **AWS S3** | 3.934.0 | File storage |
| **Axios** | 1.7.9 | HTTP client (for ML Service) |

### Cấu Trúc Thư Mục

```
backend/src/
├── config/                 # Configuration
│   └── index.ts            # Environment variables
│
├── constants/              # Constants & Messages
│   └── index.ts            # HTTP_STATUS, ERROR_MESSAGES, SUCCESS_MESSAGES
│
├── controllers/            # Request handlers
│   ├── authController.ts
│   ├── productController.ts
│   ├── CommentController.ts
│   ├── ReviewController.ts
│   ├── OrderController.ts
│   └── ...
│
├── dtos/                   # Data Transfer Objects
│   ├── UserDto.ts
│   ├── ProductDto.ts
│   ├── CommentDto.ts
│   └── ...
│
├── middleware/             # Express middlewares
│   ├── authMiddleware.ts   # JWT verification
│   ├── errorHandler.ts     # Global error handling
│   └── validationMiddleware.ts
│
├── repositories/           # Data access layer
│   ├── UserRepository.ts
│   ├── ProductRepository.ts
│   ├── CommentRepository.ts
│   └── ...
│
├── routes/                 # API route definitions
│   ├── authRoutes.ts
│   ├── productRoutes.ts
│   ├── commentRoutes.ts
│   └── ...
│
├── services/               # Business logic layer
│   ├── AuthService.ts
│   ├── ProductService.ts
│   ├── CommentService.ts   # Includes AI analysis
│   └── ...
│
├── types/                  # TypeScript types
│   └── index.ts
│
├── utils/                  # Utilities
│   ├── ApiError.ts
│   └── logger.ts
│
├── validations/            # Input validation schemas
│   ├── AuthValidation.ts
│   ├── CommentValidation.ts
│   └── ...
│
└── server.ts               # Application entry point
```

### API Endpoints

| Module | Endpoint | Mô tả |
|--------|----------|-------|
| **Auth** | `/api/auth/*` | Đăng ký, đăng nhập, refresh token |
| **Users** | `/api/users/*` | Quản lý người dùng |
| **Products** | `/api/products/*` | CRUD sản phẩm |
| **Categories** | `/api/categories/*` | Danh mục sản phẩm |
| **Brands** | `/api/brands/*` | Thương hiệu |
| **Reviews** | `/api/reviews/*` | Đánh giá sản phẩm |
| **Comments** | `/api/comments/*` | Bình luận (với AI) |
| **Cart** | `/api/cart/*` | Giỏ hàng |
| **Orders** | `/api/orders/*` | Đơn hàng |
| **Inventory** | `/api/inventory/*` | Quản lý kho |
| **Wishlist** | `/api/wishlist/*` | Danh sách yêu thích |
| **Vouchers** | `/api/admin/vouchers/*` | Mã giảm giá |
| **Payment** | `/api/payment/*` | Thanh toán |
| **Images** | `/api/images/*` | Upload hình ảnh |

### Database Schema (Prisma)

```prisma
// Các model chính
model User {
  id           String    @id @default(cuid())
  email        String    @unique
  password     String
  role         Role      @default(USER)  // USER, ADMIN, MANAGER
  // ... relations
}

model Product {
  id            String   @id @default(cuid())
  name          String
  slug          String   @unique
  basePrice     Decimal
  discount      Int
  averageRating Decimal
  // ... relations với Brand, Category, Variants, Reviews, Comments
}

model Comment {
  id         String   @id @default(cuid())
  productId  String
  userId     String
  parentId   String?           // For nested replies
  content    String
  aiAnalysis Json?             // AI sentiment analysis result
  // ... relations
}

model ProductVariantSentiment {
  id          String  @id @default(cuid())
  variantId   String  @unique
  battery     Float   @default(0)
  camera      Float   @default(0)
  performance Float   @default(0)
  display     Float   @default(0)
  design      Float   @default(0)
  price       Float   @default(0)
  shipping    Float   @default(0)
  general     Float   @default(0)
  // ... aggregated sentiment scores
}
```

### Layered Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Routes (API Endpoints)                │
│         Định nghĩa endpoints, validation middleware      │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                    Controllers                           │
│         Parse request, gọi service, format response      │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                    Services                              │
│         Business logic, validation, orchestration        │
│         Gọi ML Service cho AI analysis                   │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                    Repositories                          │
│         Data access, Prisma queries                      │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                    Database (PostgreSQL)                 │
│         Persistent storage                               │
└─────────────────────────────────────────────────────────┘
```

---

## Sentiment Analysis (AI Service)

### Tổng Quan

Hệ thống tích hợp **Aspect-Based Sentiment Analysis (ABSA)** để phân tích cảm xúc trong bình luận sản phẩm. Module AI được xây dựng sử dụng các mô hình NLP cho tiếng Việt.

### Kiến Trúc AI Integration

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AI SENTIMENT ANALYSIS FLOW                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   User Comment                                                           │
│   "Pin trâu, chụp hình đẹp nhưng giá hơi cao"                           │
│        │                                                                 │
│        ▼                                                                 │
│   ┌─────────────────────────────────────────┐                           │
│   │        Backend (CommentService)          │                           │
│   │   1. Validate content                    │                           │
│   │   2. Call ML Service                     │                           │
│   │   3. Save comment + aiAnalysis           │                           │
│   └─────────────────┬───────────────────────┘                           │
│                     │ POST /predict                                      │
│                     ▼                                                    │
│   ┌─────────────────────────────────────────┐                           │
│   │           ML Service (NLP Module)        │                           │
│   │                                          │                           │
│   │   ┌─────────────────────────────────┐   │                           │
│   │   │  NLP Pipeline                    │   │                           │
│   │   │  - Tokenization (Vietnamese)     │   │                           │
│   │   │  - Aspect Extraction             │   │                           │
│   │   │  - Sentiment Classification      │   │                           │
│   │   │  - Confidence Scoring            │   │                           │
│   │   └─────────────────────────────────┘   │                           │
│   └─────────────────┬───────────────────────┘                           │
│                     │                                                    │
│                     ▼                                                    │
│   Response:                                                              │
│   {                                                                      │
│     "results": [                                                         │
│       { "aspect": "pin", "sentiment": "positive", "confidence": 0.91 }, │
│       { "aspect": "camera", "sentiment": "positive", "confidence": 0.88 },
│       { "aspect": "giá", "sentiment": "negative", "confidence": 0.82 }  │
│     ]                                                                    │
│   }                                                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### ML Service Integration Code

```typescript
// CommentService.ts
private async analyzeComment(content: string): Promise<any> {
  try {
    const response = await axios.post(ML_SERVICE_URL, {
      text: content,
    });
    return response.data;
  } catch (error) {
    logger.error('AI Service Error:', error);
    throw error;
  }
}

// Trong createComment()
async createComment(userId: string, data: CreateCommentData): Promise<Comment> {
  // Validate content...
  
  // Analyze comment with AI
  let aiAnalysis = null;
  try {
    aiAnalysis = await this.analyzeComment(data.content);
  } catch (error) {
    // Log error but do not fail comment creation
    logger.warn('Failed to analyze comment with AI:', error);
  }

  // Create comment with AI analysis
  const comment = await this.commentRepository.create({
    ...data,
    userId,
    aiAnalysis,  // Stored as JSON in database
  });

  return comment;
}
```

### Các Aspect Được Phân Tích

| Aspect | Tiếng Việt | Mô tả |
|--------|------------|-------|
| `battery` | Pin | Thời lượng pin, sạc |
| `camera` | Camera | Chất lượng ảnh, video |
| `performance` | Hiệu năng | Tốc độ, xử lý |
| `display` | Màn hình | Độ sáng, màu sắc, độ phân giải |
| `design` | Thiết kế | Ngoại hình, chất liệu |
| `packaging` | Đóng gói | Hộp, phụ kiện |
| `price` | Giá cả | Giá trị, đắt/rẻ |
| `shopService` | Dịch vụ | Hỗ trợ, tư vấn |
| `shipping` | Giao hàng | Tốc độ, đóng gói |
| `general` | Chung | Nhận xét tổng thể |

### Sentiment Aggregation

Hệ thống tổng hợp sentiment theo từng variant sản phẩm trong bảng `ProductVariantSentiment`:

```prisma
model ProductVariantSentiment {
  id           String         @id @default(cuid())
  variantId    String         @unique
  battery      Float          @default(0)   // Trung bình sentiment pin
  camera       Float          @default(0)   // Trung bình sentiment camera
  performance  Float          @default(0)   // ...
  display      Float          @default(0)
  design       Float          @default(0)
  packaging    Float          @default(0)
  price        Float          @default(0)
  shopService  Float          @default(0)
  shipping     Float          @default(0)
  general      Float          @default(0)
  others       Float          @default(0)
  // ...
}
```

### Xử Lý Lỗi AI Service

```typescript
// Graceful degradation - AI failure không block tạo comment
try {
  aiAnalysis = await this.analyzeComment(data.content);
} catch (error) {
  logger.warn('Failed to analyze comment with AI:', error);
  // aiAnalysis remains null, comment still created
}
```

### API Request/Response

**Request:**
```http
POST /predict
Content-Type: application/json

{
  "text": "Sản phẩm chất lượng tốt, giao hàng nhanh, giá hơi cao"
}
```

**Response:**
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
      "aspect": "giá",
      "sentiment": "negative",
      "confidence": 0.75
    }
  ]
}
```

### Hiển Thị Trên UI

```
┌─────────────────────────────────────────────────────────┐
│  👤 Nguyễn Văn A                           • 2 giờ trước │
│                                                          │
│  "Sản phẩm chất lượng tốt, giao hàng nhanh, giá hơi cao"│
│                                                          │
│  [chất lượng POSITIVE] [giao hàng POSITIVE] [giá NEGATIVE]
│       (xanh lá)            (xanh lá)          (đỏ)       │
│                                                          │
│  [Trả lời]                                               │
└─────────────────────────────────────────────────────────┘
```

---

## Deployment

### Docker Compose

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: nextecommerce
    ports:
      - '5436:5432'
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

### Environment Variables

**Backend (.env):**
```env
DATABASE_URL=postgresql://user:password@localhost:5436/nextecommerce
JWT_SECRET=your-secret-key
PORT=3001
CORS_ORIGIN=http://localhost:5000
CLOUDINARY_CLOUD_NAME=xxx
CLOUDINARY_API_KEY=xxx
CLOUDINARY_API_SECRET=xxx
```

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_URL=http://localhost:3001/api
```

---

## Tóm Tắt Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Next.js 15, React 19, TypeScript, Tailwind CSS |
| **Backend** | Node.js, Express, TypeScript |
| **Database** | PostgreSQL 13, Prisma ORM |
| **Authentication** | JWT, bcrypt, HTTP-only cookies |
| **File Storage** | Cloudinary, AWS S3 |
| **AI/ML** | Sentiment Analysis (NLP for Vietnamese) |
| **DevOps** | Docker, Docker Compose |
