from playwright.sync_api import Playwright, APIRequestContext


BASE_URL = "https://rahulshettyacademy.com"


class Test_API_orderCreate:

    # ---------- FIXTURE-LIKE HELPER METHODS ----------
    def create_api_context(self, playwright: Playwright) -> APIRequestContext:
        return playwright.request.new_context(base_url=BASE_URL)

    def login(self, playwright: Playwright):
        """Login and return token + userId"""
        api = self.create_api_context(playwright)

        loginPayload = {
            "userEmail": "fepex31820@okcdeals.com",
            "userPassword": "Iamking@000"
        }

        resp = api.post("/api/ecom/auth/login", data=loginPayload)
        assert resp.ok, 'Login Successfully'

        body = resp.json()
        print("Login Response Body:", body)
        token = body["token"]
        print("Token from Response Body:", token)
        userId = body["userId"]

        print("=== LOGIN SUCCESSFUL ===")
        # print(f"Token: {token}")
        # print(f"User ID: {userId}")

        return token, userId

    # def get_cart_count(self, playwright: Playwright, token: str, userId: str) -> int:
    #     """Get items count from cart"""

    #     api = self.create_api_context(playwright)

    #     resp = api.get(
    #         f"/api/ecom/user/get-cart-count/{userId}",
    #         headers={"Authorization": f"Bearer {token}"}
    #     )
    #     assert resp.ok, "Failed to retrieve cart count!"

    #     count = resp.json()["count"]
    #     print(f"Current Cart Count: {count}")
    #     return count

    # ---------- REAL TESTS BELOW ----------

    def test_login(self, playwright: Playwright):
        token, userId = self.login(playwright)
        # cart_count = self.get_cart_count(playwright, token, userId)
        # print(f"Cart Count BEFORE adding product: {cart_count}")

    def test_createOrder(self, playwright: Playwright):
        token, userId = self.login(playwright)

        # ----------------- IMPORTANT -----------------
        # add-to-cart API expects ONLY productId, not full product details!
        orderPayload = {
  "_id": "69246f685008f6a909377d5a",
  "product": {
    "_id": "68a961459320a140fe1ca57a",
    "productName": "ZARA COAT 3",
    "productCategory": "electronics",
    "productSubCategory": "mobiles",
    "productPrice": 11500,
    "productDescription": "Apple phone",
    "productImage": "https://rahulshettyacademy.com/api/ecom/uploads/productImage_1650649434146.jpeg",
    "productRating": "0",
    "productTotalOrders": "0",
    "productStatus": 'true',
    "productFor": "women",
    "productAddedBy": "admin",
    "__v": 0
  }
        }
        api = self.create_api_context(playwright)
        resp = api.post(
            "/api/ecom/user/add-to-cart",
            data=orderPayload,
            headers={"Authorization": '{token}'}
        )
        assert resp.ok, "Product Added To Cart"

        print("Product added to cart successfully.")

        # Validate updated cart count
        # updated_count = self.get_cart_count(playwright, token, userId)
        # print(f"Cart Count AFTER adding product: {updated_count}")

        print("===== ORDER CREATION WORKFLOW COMPLETED =====")
