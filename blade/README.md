## 🛠️ ROUTES TO IMPLEMENT


| **METHOD** | **ROUTE**                 | **FUNCTIONALITY**                     | **ACCESS**      |
|------------|---------------------------|---------------------------------------|-----------------|
| `POST`     | `/auth/signup`            | Register new User         | Public          |
| `POST`     | `/auth/login`             | User login and authentication         | Public          |
| `POST`     | `/customers/register`     | Register a new customer               | Public          |
| `GET`      | `/customers/{customer_id}`| Retrieve customer details             | Authenticated   |
| `POST`     | `/orders`                 | Create a new sharpening order         | Authenticated   |
| `GET`      | `/orders/{order_id}/status`| Check order status                    | Authenticated   |
| `GET`      | `/pricing`                | Retrieve service pricing              | Public          |

---

## Notes:

- **Access Levels**:
  - **Public**: No authentication required.
  - **Authenticated**: Requires a valid authentication token.

- Use the base URL:  
