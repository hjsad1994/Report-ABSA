# Nghiên cứu Ứng dụng Trí tuệ Nhân tạo trong Dự đoán Mức độ Hài lòng Khách hàng qua Phân tích Cảm xúc Bình luận Sản phẩm

## Tổng quan nghiên cứu
Nghiên cứu này trình bày việc phát triển hệ thống thương mại điện tử VeritaShop, một nền tảng tích hợp trí tuệ nhân tạo tiên tiến để phân tích và dự đoán mức độ hài lòng của khách hàng thông qua xử lý ngôn ngữ tự nhiên. Hệ thống được thiết kế với khả năng phân tích cảm xúc từ bình luận sản phẩm một cách tự động và chính xác, sử dụng mô hình học sâu PhoBERT được huấn luyện chuyên sâu cho ngôn ngữ tiếng Việt.

Điểm nổi bật của nghiên cứu nằm ở việc áp dụng các kỹ thuật machine learning hiện đại để giải quyết bài toán phân tích cảm xúc (sentiment analysis) trong lĩnh vực thương mại điện tử, góp phần nâng cao trải nghiệm người dùng và hỗ trợ doanh nghiệp trong việc ra quyết định dựa trên dữ liệu thực tế từ phản hồi khách hàng.

## Mục tiêu nghiên cứu
Nghiên cứu hướng tới việc phát triển một hệ thống phân tích cảm xúc sản phẩm hoàn chỉnh, tích hợp khả năng dự đoán mức độ hài lòng khách hàng thông qua bình luận trực tuyến. Hệ thống được thiết kế để:

1. **Tự động hóa quy trình phân tích cảm xúc** từ bình luận sản phẩm bằng mô hình học sâu tiên tiến
2. **Cung cấp dự đoán chính xác** về mức độ hài lòng (tích cực, tiêu cực, trung tính) cho doanh nghiệp
3. **Hỗ trợ ra quyết định dựa trên dữ liệu** thực tế từ phản hồi khách hàng
4. **Nâng cao trải nghiệm người dùng** thông qua giao diện trực quan và cá nhân hóa

## Ý nghĩa khoa học và thực tiễn

### Đối với doanh nghiệp:
- **Phân tích cảm xúc tiên tiến:** Áp dụng mô hình PhoBERT được tối ưu hóa cho tiếng Việt để đạt độ chính xác cao trong phân tích cảm xúc đa chiều
- **Dự đoán hành vi khách hàng:** Tự động phân loại và dự đoán mức độ hài lòng từ bình luận thực tế, hỗ trợ doanh nghiệp nắm bắt nhanh chóng phản hồi thị trường
- **Ra quyết định chiến lược:** Cung cấp insights khoa học từ dữ liệu thực tế để tối ưu hóa sản phẩm và dịch vụ

### Đối với người dùng:
- **Thông tin đáng tin cậy:** Nhận được phân tích cảm xúc minh bạch và chính xác từ cộng đồng người dùng thực tế
- **Hỗ trợ quyết định mua hàng:** Dựa vào phân tích khoa học để đưa ra lựa chọn sản phẩm sáng suốt
- **Trải nghiệm nâng cao:** Tương tác với hệ thống AI để nhận gợi ý và hỗ trợ cá nhân hóa

## Kiến trúc hệ thống nghiên cứu
Nghiên cứu áp dụng kiến trúc **Microservices** để đảm bảo tính linh hoạt, khả năng mở rộng và bảo trì độc lập cho từng thành phần chức năng. Kiến trúc này cho phép phát triển, triển khai và mở rộng từng dịch vụ một cách độc lập, phù hợp với yêu cầu của một hệ thống thương mại điện tử phức tạp với tích hợp trí tuệ nhân tạo.

Mỗi microservice được thiết kế theo mô hình **Layered Architecture** với sự phân tách rõ ràng giữa các lớp chức năng, đảm bảo tính mô-đun cao và dễ dàng bảo trì trong quá trình nghiên cứu và phát triển.

### Layered Architecture cho Microservices

**Presentation Layer (Controllers):**
- Nhận và xử lý HTTP requests từ client
- Validation input data và authentication/authorization
- Trả về responses với định dạng phù hợp (JSON/XML)
- Error handling và logging

**Business Logic Layer (Services):**
- Chứa logic nghiệp vụ cốt lõi của ứng dụng
- Xử lý các use cases và business rules
- Giao tiếp với Data Access Layer
- Transaction management và business validations

**Data Access Layer (Repositories):**
- Tương tác trực tiếp với cơ sở dữ liệu
- Thực hiện CRUD operations
- Query optimization và caching strategies
- Data mapping và transformation

**Database Layer:**
- PostgreSQL cho dữ liệu có cấu trúc (users, products, orders)
- MongoDB cho dữ liệu phân tích và logs
- Prisma ORM để truy cập database type-safe
- Connection pooling và query optimization

### Design Patterns

**Saga Pattern:**
- Áp dụng cho các giao dịch phân tán giữa các microservices
- Đảm bảo tính nhất quán dữ liệu (Data Consistency) trong hệ thống phân tán
- Xử lý các business transaction phức tạp như đặt hàng, thanh toán
- Có thể implement bằng:
  - Choreography-based Saga (event-driven)
  - Orchestration-based Saga (coordinator service)

## Công nghệ và Phương pháp Nghiên cứu - Thứ tự ưu tiên phát triển

### 1. **Trí tuệ Nhân tạo và Học máy (Ưu tiên cao nhất)**

**Kiến trúc Mô hình và Framework:**
- **PhoBERT (Pham et al., 2020):** Mô hình ngôn ngữ BERT được huấn luyện trước dành riêng cho tiếng Việt, đạt hiệu suất state-of-the-art trên các tác vụ NLP tiếng Việt
- **Transformers (Hugging Face):** Thư viện xử lý ngôn ngữ tự nhiên tiên tiến với các mô hình pretrained đa dạng và pretrained weights
- **PyTorch:** Framework học sâu mạnh mẽ để fine-tuning và triển khai mô hình PhoBERT trong môi trường production với hỗ trợ GPU
- **Scikit-learn:** Thư viện machine learning toàn diện cho tiền xử lý dữ liệu và đánh giá mô hình phân loại với các metrics chi tiết

**Phương pháp Xử lý Ngôn ngữ Tự nhiên:**
- **VNCoreNLP:** Công cụ phân đoạn từ chuyên dụng cho tiếng Việt, đảm bảo độ chính xác cao trong việc nhận diện từ ghép
- **Pipeline Tiền xử lý:** Quy trình chuẩn hóa dữ liệu toàn diện bao gồm lowercase, chuẩn hóa từ viết tắt, loại bỏ dấu câu, chuyển đổi biểu tượng cảm xúc
- **Thu thập và Gán nhãn Dữ liệu:** Bộ dữ liệu gồm 15.000 bình luận thực tế từ các nền tảng thương mại điện tử lớn, được gán nhãn cảm xúc bởi chuyên gia lĩnh vực

### 2. **Backend (Microservices)**

**Ngôn ngữ:**
- Python & NodeJS với TypeScript

**Cấu trúc Services:**
- **AI Service:** Python (FastAPI) - Tối ưu cho ML inference với async support và auto-documented API
- **User/Auth Service, Product Service, Payment Service:** Node.js (Express.js) - Mạnh mẽ cho I/O, xây dựng REST API nhanh chóng

**Giao tiếp giữa các service:**
- REST API hoặc Message Queue (RabbitMQ/Kafka) cho giao tiếp bất đồng bộ

**Xác thực & Database:**
- **JWT:** Xác thực người dùng với token mã hóa an toàn
- **Prisma ORM:** Type-safe database access, auto-generated clients, migrations tự động
- **PostgreSQL:** Cơ sở dữ liệu chính cho users, products, orders
- **MongoDB:** Lưu trữ dữ liệu phân tích, logs và cache

### 3. **DevOps & Infrastructure**

**Containerization & Orchestration:**
- **Docker:** Container hóa AI service và microservices với multi-stage builds
- **Docker Compose:** Phát triển local và staging với environment riêng biệt
- **Kubernetes (K8s):** Orchestration production với auto-scaling cho AI workloads

**CI/CD:**
- **GitHub Actions:** Pipeline tự động cho testing, building, deployment
- **Multi-environment:** Dev, staging, prod với config riêng biệt

**Cloud Platform:**
- **AWS (Primary):** EKS, RDS, S3, ECR, API Gateway, CloudWatch, ELB
- **Azure/GCP (Backup):** Container services và managed databases

**Monitoring & Logging:**
- **Prometheus & Grafana:** Monitoring metrics cho AI model performance
- **ELK Stack:** Centralized logging với Elasticsearch, Logstash, Kibana

### 4. **Frontend (Cuối cùng)**

**Web App:**
- **Next.js:** React framework với SSR/SSG, App Router, Server Components
- **State Management:** Redux Toolkit cho state phức tạp
- **UI Library:** Material-UI (MUI) hoặc Ant Design với theme tùy chỉnh

**Mobile App:**
- **Flutter:** Framework đa nền tảng với Dart, hot reload
- **State Management:** BLoC pattern hoặc Riverpod
- **UI:** Material Design & Cupertino với responsive design
- **HTTP Client:** Dio cho API calls với interceptor và retry logic

### Cơ sở dữ liệu (Database)

**Relational DB:**
- **PostgreSQL:** Cơ sở dữ liệu chính cho users, products, orders với ACID compliance
- **Connection Pooling:** PgBouncer để tối ưu kết nối database

**NoSQL DB:**
- **MongoDB:** Lưu trữ dữ liệu phân tích cảm xúc, logs và cache với schema linh hoạt
- **Redis:** Caching layer cho session, API responses và dữ liệu tạm thời

**ORM & Database Tools:**
- **Prisma:** Type-safe ORM cho Node.js, auto-generated clients, migrations tự động
- **Database Monitoring:** PgHero cho PostgreSQL performance monitoring

### Infrastructure Architecture

**Kubernetes Deployment (VeritaShop):**
- **Namespaces:** Separate environments (dev, staging, prod) với RBAC
- **Pods:** AI service và microservices chạy trong containers được tối ưu
- **Services:** Service discovery với load balancing cho AI inference requests
- **Ingress:** Route traffic với rate limiting và SSL termination
- **ConfigMaps & Secrets:** Quản lý model weights và API keys an toàn
- **PersistentVolumes:** Storage cho training data và model artifacts
- **Horizontal Pod Autoscaling:** Auto-scaling dựa trên AI workload demands

**Microservices trên K8s:**
- **AI Service (Python + FastAPI):** Phân tích cảm xúc với GPU support nếu cần
- **User/Auth Service (Node.js + Express.js + Prisma):** Xác thực và quản lý người dùng
- **Product Service (Node.js + Express.js + Prisma):** Catalog và inventory management
- **Payment Service (Node.js + Express.js + Prisma):** Thanh toán với distributed transactions
- **Web App (Next.js):** SSR với cached sentiment analysis results
- **Mobile App (Flutter):** Native apps với offline sentiment caching

## Các thành phần chính cần phát triển (Thứ tự ưu tiên)

### 1. **Mô hình PhoBERT (Ưu tiên cao nhất)**
   - **Kiến trúc PhoBERT:** Mô hình ngôn ngữ BERT-base (12 layers, 768 hidden dimensions, 12 attention heads) được huấn luyện trước trên 20GB dữ liệu tiếng Việt sạch
   - **Phân tích cảm xúc:** Fine-tuning PhoBERT với focal loss để dự đoán 3 lớp cảm xúc (tích cực, tiêu cực, trung tính) từ bình luận sản phẩm
   - **Xử lý ngôn ngữ tự nhiên:** Sử dụng VNCoreNLP cho word segmentation và PyVi cho xử lý từ ghép tiếng Việt
   - **Đánh giá mô hình:** Validation với cross-validation, metrics precision, recall, F1-score trên tập test độc lập

### 2. **Microservices Backend (với Layered Architecture)**
   - **AI Service (Python + FastAPI):** API endpoint cho phân tích cảm xúc với mô hình PhoBERT được tổ chức theo layers (Controller → Service → Repository)
   - **User/Auth Service (Node.js + Express.js + Prisma):** Xác thực JWT, quản lý người dùng với PostgreSQL theo mô hình phân lớp
   - **Product Service (Node.js + Express.js + Prisma):** Quản lý sản phẩm, đánh giá với PostgreSQL theo kiến trúc phân lớp
   - **Payment Service (Node.js + Express.js + Prisma):** Xử lý thanh toán với Saga Pattern và kiến trúc phân lớp rõ ràng

### 3. **DevOps Pipeline**
   - **Containerization:** Docker và Docker Compose cho AI service và microservices
   - **Orchestration:** Kubernetes (K8s) cho deployment và scaling tự động
   - **CI/CD:** GitHub Actions cho automated testing và deployment
   - **Monitoring:** Prometheus, Grafana cho theo dõi hiệu suất AI model
   - **Logging:** ELK Stack cho log tập trung và debugging

### 4. **Frontend (Cuối cùng)**
   - **Web App (Next.js):** Giao diện hiển thị kết quả phân tích cảm xúc với SSR/SSG
   - **Mobile App (Flutter):** Ứng dụng đồng bộ cho Android và iOS
   - **UI/UX:** Material-UI cho web, Flutter widgets cho mobile với responsive design

## Các tính năng chính (Ưu tiên AI)

### 🤖 **AI-Powered Features (Core)**
- **Phân tích cảm xúc PhoBERT:** Sử dụng mô hình BERT-base pretrained fine-tuned với focal loss cho sentiment analysis 3 lớp (tích cực/tiêu cực/trung tính)
- **Confidence scoring:** Cung cấp confidence score và attention weights để giải thích kết quả dự đoán
- **Real-time sentiment analysis:** Phân tích cảm xúc với low-latency inference (< 50ms) sử dụng GPU acceleration
- **Sentiment trend analysis:** Dashboard trực quan hiển thị xu hướng cảm xúc theo thời gian và category với interactive visualizations

### 🛒 **E-commerce Features**
- **Smart product discovery:** Gợi ý sản phẩm dựa trên sentiment analysis
- **Đánh giá sản phẩm:** Người dùng đánh giá với sentiment tracking
- **Shopping cart & checkout:** Thanh toán an toàn với Saga Pattern
- **Order management:** Theo dõi đơn hàng với distributed transactions

### 📱 **User Experience**
- **Responsive design:** Web và mobile với giao diện đồng nhất
- **AI chatbot:** Hỗ trợ khách hàng với hiểu biết về sentiment
- **Personalized recommendations:** Gợi ý dựa trên lịch sử cảm xúc

### ⚡ **Technical Excellence**
- **Layered Architecture:** Tách biệt rõ ràng các lớp (Controller → Service → Repository) cho dễ bảo trì và mở rộng
- **Modular Design:** Mỗi microservice được tổ chức theo mô hình phân lớp để tăng tính tái sử dụng
- **Auto-scaling:** Kubernetes HPA cho AI workloads với horizontal scaling
- **Real-time monitoring:** Prometheus/Grafana cho model performance và service health
- **Centralized logging:** ELK Stack cho debugging và analytics toàn hệ thống
- **SEO optimization:** Next.js SSR với cached sentiment data

---

## Lộ trình Nghiên cứu và Phát triển - Thứ tự ưu tiên

### 🚀 **Giai đoạn 1: Tập trung Trí tuệ Nhân tạo (Ưu tiên cao nhất)**
1. **Phát triển Mô hình PhoBERT** - Fine-tuning mô hình BERT-base pretrained cho sentiment analysis trên bộ dữ liệu 15.000 bình luận tiếng Việt với focal loss
2. **Tối ưu và Validation** - Cross-validation, hyperparameter tuning và evaluation metrics (precision, recall, F1-score)
3. **Triển khai AI Service** - FastAPI service với PyTorch model loading và GPU inference optimization

### 🏗️ **Giai đoạn 2: Nền tảng Backend**
4. **Thiết kế Kiến trúc Phân lớp** - Xây dựng mô hình layered architecture (Controller → Service → Repository) cho từng microservice
5. **Phát triển Microservices** - Triển khai các dịch vụ Node.js với Express.js và Prisma ORM theo nguyên tắc phân lớp
6. **Tích hợp Cơ sở dữ liệu** - Cấu hình PostgreSQL + MongoDB với connection pooling và repository pattern
7. **Bảo mật và Xác thực** - Triển khai hệ thống JWT-based authentication với refresh tokens và middleware bảo mật

### ☁️ **Giai đoạn 3: Vận hành và Mở rộng**
8. **Container hóa Ứng dụng** - Xây dựng Docker multi-stage builds cho AI và backend services
9. **Triển khai Kubernetes** - Thiết lập môi trường production với khả năng auto-scaling
10. **Giám sát và Ghi log** - Cấu hình hệ thống monitoring Prometheus/Grafana và ELK Stack

### 🎨 **Giai đoạn 4: Giao diện Người dùng**
11. **Ứng dụng Web (Next.js)** - Phát triển giao diện với SSR và cached sentiment analysis
12. **Ứng dụng Di động (Flutter)** - Xây dựng ứng dụng đa nền tảng với khả năng offline

*Memory Bank này sẽ được cập nhật liên tục trong quá trình nghiên cứu và phát triển hệ thống VeritaShop, với trọng tâm nghiên cứu về mô hình PhoBERT và focal loss trong sentiment analysis, theo thứ tự ưu tiên AI → Backend → DevOps → Frontend.*
