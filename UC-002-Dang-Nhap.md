# Use Case: Đăng Nhập

## Thông Tin Chung

| Thuộc tính | Mô tả |
|------------|-------|
| **Use Case ID** | UC-002 |
| **Use Case Name** | Đăng Nhập (User Login) |
| **Actor** | Khách (Guest User), Người dùng đã đăng ký |
| **Description** | Cho phép người dùng đã có tài khoản đăng nhập vào hệ thống VeritaShop bằng email và mật khẩu. Sau khi đăng nhập thành công, hệ thống chuyển hướng người dùng đến trang phù hợp với vai trò của họ. |

---

## Điều Kiện

| Loại | Mô tả |
|------|-------|
| **Preconditions** | 1. Người dùng chưa đăng nhập vào hệ thống<br>2. Người dùng đã có tài khoản trong hệ thống<br>3. Người dùng truy cập được trang đăng nhập (/login) |
| **Postconditions** | 1. Người dùng được xác thực thành công<br>2. Access token và Refresh token được lưu vào cookies<br>3. Người dùng được chuyển hướng đến trang phù hợp với vai trò |
| **Trigger** | Người dùng nhấn vào link "Sign in" hoặc truy cập trực tiếp URL /login |

---

## Luồng Xử Lý

### Normal Flow (Luồng Chính)

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Truy cập trang đăng nhập | Kiểm tra trạng thái xác thực hiện tại |
| 2 | - | Nếu đã đăng nhập → chuyển hướng theo vai trò |
| 3 | - | Hiển thị form đăng nhập với các trường: Email, Password, Remember me |
| 4 | Nhập địa chỉ email | - |
| 5 | Nhập mật khẩu | - |
| 6 | (Tùy chọn) Tick "Remember me" | - |
| 7 | Nhấn nút "Sign in" | - |
| 8 | - | Validate dữ liệu đầu vào (frontend) |
| 9 | - | Gửi request POST /api/auth/login |
| 10 | - | Backend tìm user theo email |
| 11 | - | So sánh mật khẩu đã hash |
| 12 | - | Tạo Access Token (JWT) và Refresh Token |
| 13 | - | Lưu Refresh Token vào database |
| 14 | - | Trả về thông tin user và tokens |
| 15 | - | Lưu tokens vào cookies (httpOnly, secure) |
| 16 | - | Hiển thị thông báo "Login successful!" |
| 17 | - | Chuyển hướng theo vai trò người dùng |

### Chuyển hướng theo vai trò:
| Vai trò | Trang đích |
|---------|------------|
| ADMIN | /admin |
| MANAGER | /admin |
| USER | / (hoặc trang đã lưu trong redirectPath) |

---

### Alternative Flows (Luồng Thay Thế)

#### AF-1: Đăng nhập qua Google
| Bước | Mô tả |
|------|-------|
| 1 | Từ bước 3, người dùng nhấn nút "Google" |
| 2 | Hệ thống chuyển hướng đến Google OAuth |
| 3 | Người dùng xác thực với Google |
| 4 | Google trả về thông tin user |
| 5 | Tiếp tục từ bước 12 của Normal Flow |

#### AF-2: Đăng nhập qua GitHub
| Bước | Mô tả |
|------|-------|
| 1 | Từ bước 3, người dùng nhấn nút "GitHub" |
| 2 | Hệ thống chuyển hướng đến GitHub OAuth |
| 3 | Người dùng xác thực với GitHub |
| 4 | GitHub trả về thông tin user |
| 5 | Tiếp tục từ bước 12 của Normal Flow |

#### AF-3: Có redirect path đã lưu
| Bước | Mô tả |
|------|-------|
| 1 | Người dùng truy cập trang yêu cầu xác thực (VD: /checkout) |
| 2 | Hệ thống lưu redirect path vào sessionStorage |
| 3 | Chuyển hướng đến trang login |
| 4 | Sau khi đăng nhập thành công (bước 16) |
| 5 | Chuyển hướng về trang đã lưu thay vì trang mặc định |
| 6 | Xóa redirect path khỏi sessionStorage |

#### AF-4: Quên mật khẩu
| Bước | Mô tả |
|------|-------|
| 1 | Từ bước 3, người dùng nhấn "Forgot password?" |
| 2 | Chuyển hướng đến trang /forgot-password |
| 3 | (Xem Use Case UC-003: Quên Mật Khẩu) |

---

### Exception Flows (Luồng Ngoại Lệ)

#### EX-1: Email không tồn tại
| Bước | Mô tả |
|------|-------|
| Điều kiện | Email chưa được đăng ký trong hệ thống |
| Xử lý | Hiển thị thông báo "Invalid credentials" |
| Kết quả | Người dùng nhập lại thông tin hoặc đăng ký tài khoản mới |

#### EX-2: Mật khẩu không đúng
| Bước | Mô tả |
|------|-------|
| Điều kiện | Mật khẩu không khớp với mật khẩu đã lưu |
| Xử lý | Hiển thị thông báo "Invalid credentials" |
| Kết quả | Người dùng nhập lại mật khẩu hoặc sử dụng "Forgot password" |

#### EX-3: Thiếu email hoặc mật khẩu
| Bước | Mô tả |
|------|-------|
| Điều kiện | Người dùng không nhập email hoặc mật khẩu |
| Xử lý | Hiển thị thông báo "Please enter both email and password" |
| Kết quả | Người dùng điền đầy đủ thông tin |

#### EX-4: Email không hợp lệ
| Bước | Mô tả |
|------|-------|
| Điều kiện | Email không đúng định dạng |
| Xử lý | Hiển thị thông báo "Please provide a valid email address" |
| Kết quả | Người dùng sửa email theo đúng định dạng |

#### EX-5: Lỗi kết nối server
| Bước | Mô tả |
|------|-------|
| Điều kiện | Server không phản hồi hoặc lỗi mạng |
| Xử lý | Hiển thị thông báo "Login failed. Please check your credentials." |
| Kết quả | Người dùng thử đăng nhập lại |

#### EX-6: Đã đăng nhập
| Bước | Mô tả |
|------|-------|
| Điều kiện | Người dùng đã có phiên đăng nhập hợp lệ |
| Xử lý | Tự động chuyển hướng đến trang phù hợp với vai trò |
| Kết quả | Không cần đăng nhập lại |

---

## Business Rules

| Rule ID | Mô tả |
|---------|-------|
| BR-001 | Email và mật khẩu là bắt buộc |
| BR-002 | Hệ thống không phân biệt lỗi email không tồn tại hay mật khẩu sai (bảo mật) |
| BR-003 | Access Token có thời hạn ngắn (1 giờ) |
| BR-004 | Refresh Token có thời hạn dài hơn (cấu hình trong config) |
| BR-005 | Tokens được lưu trong cookies với httpOnly và secure flags |
| BR-006 | Admin/Manager được chuyển hướng đến /admin |
| BR-007 | User thường được chuyển hướng đến / hoặc trang đã lưu |

---

## UI Elements

| Element | Loại | Bắt buộc | Mô tả |
|---------|------|----------|-------|
| Email | Email input | Có | Địa chỉ email đăng ký |
| Password | Password input | Có | Mật khẩu tài khoản |
| Show/Hide Password | Toggle button | Không | Hiển thị/ẩn mật khẩu |
| Remember me | Checkbox | Không | Ghi nhớ đăng nhập |
| Forgot password | Link | - | Chuyển đến trang quên mật khẩu |
| Sign in | Button | - | Submit form |
| Google | Button | - | OAuth Google |
| GitHub | Button | - | OAuth GitHub |
| Sign up | Link | - | Chuyển đến trang đăng ký |

---

## API Endpoints

| Method | Endpoint | Request Body | Response |
|--------|----------|--------------|----------|
| POST | `/api/auth/login` | `{ email, password }` | `{ success: true, message, data: { user } }` |
| POST | `/api/auth/refresh` | (cookies) | `{ success: true, message, data: null }` |
| POST | `/api/auth/logout` | (cookies) | `{ success: true, message, data: null }` |

---

## Token Management

### Access Token (JWT)
```json
{
  "userId": "uuid",
  "email": "user@example.com",
  "role": "USER | ADMIN | MANAGER"
}
```

### Cookie Configuration
| Cookie | HttpOnly | Secure | SameSite | MaxAge |
|--------|----------|--------|----------|--------|
| accessToken | Yes | Yes (production) | Strict | 1 hour |
| refreshToken | Yes | Yes (production) | Strict | Config value |

---

## Sequence Diagram Reference

```
Khách → Trang Đăng Nhập → Check Auth Status → Frontend Validation 
→ API Login → Find User → Verify Password → Generate Tokens 
→ Save Refresh Token → Set Cookies → Redirect by Role
```
