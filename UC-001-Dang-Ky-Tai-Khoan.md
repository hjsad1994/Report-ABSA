# Use Case: Đăng Ký Tài Khoản

## Thông Tin Chung

| Thuộc tính | Mô tả |
|------------|-------|
| **Use Case ID** | UC-001 |
| **Use Case Name** | Đăng Ký Tài Khoản (User Registration) |
| **Actor** | Khách (Guest User) |
| **Description** | Cho phép người dùng mới tạo tài khoản trên hệ thống VeritaShop bằng cách cung cấp thông tin cá nhân (họ tên, email, mật khẩu). Sau khi đăng ký thành công, hệ thống tự động đăng nhập cho người dùng. |

---

## Điều Kiện

| Loại | Mô tả |
|------|-------|
| **Preconditions** | 1. Người dùng chưa đăng nhập vào hệ thống<br>2. Người dùng truy cập được trang đăng ký (/register)<br>3. Email đăng ký chưa tồn tại trong hệ thống |
| **Postconditions** | 1. Tài khoản mới được tạo và lưu vào database<br>2. Người dùng được tự động đăng nhập<br>3. Người dùng được chuyển hướng về trang chủ |
| **Trigger** | Người dùng nhấn vào link "Create Account" hoặc truy cập trực tiếp URL /register |

---

## Luồng Xử Lý

### Normal Flow (Luồng Chính)

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Truy cập trang đăng ký | Hiển thị form đăng ký với các trường: Họ tên, Email, Mật khẩu, Xác nhận mật khẩu, Checkbox điều khoản |
| 2 | Nhập họ tên đầy đủ | - |
| 3 | Nhập địa chỉ email | - |
| 4 | Nhập mật khẩu (tối thiểu 6 ký tự, gồm chữ hoa, chữ thường, số) | - |
| 5 | Nhập lại mật khẩu để xác nhận | - |
| 6 | Tick checkbox đồng ý Điều khoản dịch vụ và Chính sách bảo mật | - |
| 7 | Nhấn nút "Create account" | - |
| 8 | - | Validate dữ liệu đầu vào (frontend) |
| 9 | - | Gửi request POST /api/auth/register |
| 10 | - | Backend validate dữ liệu |
| 11 | - | Kiểm tra email chưa tồn tại |
| 12 | - | Hash mật khẩu và lưu user mới |
| 13 | - | Trả về thông báo thành công |
| 14 | - | Tự động đăng nhập (gọi API login) |
| 15 | - | Lưu tokens vào cookies |
| 16 | - | Hiển thị thông báo "Registration successful!" |
| 17 | - | Chuyển hướng về trang chủ (/) |

---

### Alternative Flows (Luồng Thay Thế)

#### AF-1: Đăng ký qua Google
| Bước | Mô tả |
|------|-------|
| 1 | Từ bước 1, người dùng nhấn nút "Google" |
| 2 | Hệ thống chuyển hướng đến Google OAuth |
| 3 | Người dùng xác thực với Google |
| 4 | Google trả về thông tin user |
| 5 | Tiếp tục từ bước 11 của Normal Flow |

#### AF-2: Đăng ký qua GitHub
| Bước | Mô tả |
|------|-------|
| 1 | Từ bước 1, người dùng nhấn nút "GitHub" |
| 2 | Hệ thống chuyển hướng đến GitHub OAuth |
| 3 | Người dùng xác thực với GitHub |
| 4 | GitHub trả về thông tin user |
| 5 | Tiếp tục từ bước 11 của Normal Flow |

#### AF-3: Tự động đăng nhập thất bại
| Bước | Mô tả |
|------|-------|
| 1 | Sau bước 13, việc tự động đăng nhập thất bại |
| 2 | Hiển thị thông báo "Registration successful. Please login manually." |
| 3 | Chuyển hướng đến trang đăng nhập (/login) |

---

### Exception Flows (Luồng Ngoại Lệ)

#### EX-1: Email đã tồn tại
| Bước | Mô tả |
|------|-------|
| Điều kiện | Email đã được đăng ký trong hệ thống |
| Xử lý | Hiển thị thông báo lỗi "Email already exists" |
| Kết quả | Người dùng quay lại form, nhập email khác |

#### EX-2: Mật khẩu không hợp lệ
| Bước | Mô tả |
|------|-------|
| Điều kiện | Mật khẩu < 6 ký tự hoặc thiếu chữ hoa/chữ thường/số |
| Xử lý | Hiển thị thông báo "Password must be at least 6 characters long" hoặc "Password must contain at least one uppercase letter, one lowercase letter, and one number" |
| Kết quả | Người dùng sửa mật khẩu theo yêu cầu |

#### EX-3: Mật khẩu không khớp
| Bước | Mô tả |
|------|-------|
| Điều kiện | Mật khẩu và xác nhận mật khẩu không giống nhau |
| Xử lý | Hiển thị thông báo "Passwords do not match" |
| Kết quả | Người dùng nhập lại mật khẩu |

#### EX-4: Chưa đồng ý điều khoản
| Bước | Mô tả |
|------|-------|
| Điều kiện | Người dùng chưa tick checkbox điều khoản |
| Xử lý | Hiển thị thông báo "Please accept the terms and conditions" |
| Kết quả | Người dùng tick checkbox và thử lại |

#### EX-5: Email không hợp lệ
| Bước | Mô tả |
|------|-------|
| Điều kiện | Email không đúng định dạng (ví dụ: thiếu @, thiếu domain) |
| Xử lý | Hiển thị thông báo "Please provide a valid email address" |
| Kết quả | Người dùng sửa email theo đúng định dạng |

#### EX-6: Lỗi kết nối server
| Bước | Mô tả |
|------|-------|
| Điều kiện | Server không phản hồi hoặc lỗi mạng |
| Xử lý | Hiển thị thông báo "Registration failed. Please try again." |
| Kết quả | Người dùng thử đăng ký lại |

---

## Business Rules

| Rule ID | Mô tả |
|---------|-------|
| BR-001 | Email phải là duy nhất trong hệ thống |
| BR-002 | Mật khẩu tối thiểu 6 ký tự |
| BR-003 | Mật khẩu phải chứa ít nhất 1 chữ hoa, 1 chữ thường, 1 số |
| BR-004 | Họ tên (nếu có) phải từ 2-50 ký tự |
| BR-005 | Người dùng phải đồng ý Điều khoản dịch vụ và Chính sách bảo mật |

---

## UI Elements

| Element | Loại | Bắt buộc | Validation |
|---------|------|----------|------------|
| Full name | Text input | Không | 2-50 ký tự |
| Email | Email input | Có | Định dạng email hợp lệ |
| Password | Password input | Có | Min 6 ký tự, có chữ hoa, chữ thường, số |
| Confirm Password | Password input | Có | Phải khớp với Password |
| Terms checkbox | Checkbox | Có | Phải được tick |
| Create account | Button | - | Submit form |
| Google | Button | - | OAuth Google |
| GitHub | Button | - | OAuth GitHub |

---

## API Endpoints

| Method | Endpoint | Request Body | Response |
|--------|----------|--------------|----------|
| POST | `/api/auth/register` | `{ email, password, name? }` | `{ success: true, message, data: { user } }` |
| POST | `/api/auth/login` | `{ email, password }` | `{ success: true, message, data: { user } }` |

---

## Sequence Diagram Reference

```
Khách → Trang Đăng Ký → Frontend Validation → API Register → Backend Validation 
→ Database Check → Create User → Auto Login → Redirect Home
```
