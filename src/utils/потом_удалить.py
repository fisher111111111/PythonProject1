#
# from typing import Optional, Dict, Any
# import requests
#
# class RestfulBookerClient:
#     def __init__(self, base_url: str = "https://restful-booker.herokuapp.com"):
#         self.base_url = base_url.rstrip("/")
#         self.session = requests.Session()
#         self.token: Optional[str] = None
#
#     def _url(self, path: str) -> str:
#         return f"{self.base_url}/{path}"
#
#     def _handle_response(self, resp: requests.Response) -> Any:
#         try:
#             data = resp.json()
#         except ValueError:
#             resp.raise_for_status()
#             return resp.text
#         if not resp.ok:
#             raise requests.HTTPError(f"{resp.status_code} Error: {data}", response=resp)
#         return data
#
#     def create_token(self, username: str, password: str) -> str:
#         url = self._url("/auth")
#         resp = self.session.post(url, json={"username": username, "password": password})
#         data = self._handle_response(resp)
#         token = data.get("token")
#         if not token:
#             raise RuntimeError("Token not returned")
#         self.token = token
#         self.session.headers.update({"Cookie": f"token={token}"})
#         return token
#
#     def create_booking(self, booking: Dict[str, Any]) -> Dict[str, Any]:
#         url = self._url("/booking")
#         resp = self.session.post(url, json=booking, headers={"Content-Type": "application/json"})
#         return self._handle_response(resp)
#
#     def get_booking(self, booking_id: int) -> Dict[str, Any]:
#         url = self._url(f"/booking/{booking_id}")
#         resp = self.session.get(url, headers={"Accept": "application/json"})
#         return self._handle_response(resp)
#
#     def update_booking(self, booking_id: int, booking: Dict[str, Any]) -> Dict[str, Any]:
#         url = self._url(f"/booking/{booking_id}")
#         resp = self.session.put(url, json=booking, headers={"Content-Type": "application/json"})
#         return self._handle_response(resp)
#
#     def partial_update_booking(self, booking_id: int, partial: Dict[str, Any]) -> Dict[str, Any]:
#         url = self._url(f"/booking/{booking_id}")
#         resp = self.session.patch(url, json=partial, headers={"Content-Type": "application/json"})
#         return self._handle_response(resp)
#
#     def delete_booking(self, booking_id: int) -> bool:
#         url = self._url(f"/booking/{booking_id}")
#         resp = self.session.delete(url)
#         if resp.status_code == 201:
#             return True
#         self._handle_response(resp)
#         return False
#
#     def get_bookings(self, params: Optional[Dict[str, Any]] = None) -> Any:
#         """
#         Получить список id бронирований (GET /booking)
#         Можно передать filters в params: firstname, lastname, checkin, checkout
#         """
#         url = self._url("/booking")
#         resp = self.session.get(url, params=params)
#         return self._handle_response(resp)
#
#     def set_basic_auth(self, username: str, password: str):
#         self.session.auth = (username, password)
#
#     def close(self):
#         self.session.close()
#
#
# # Пример использования
# if __name__ == "__main__":
#     client = RestfulBookerClient()
#     booking_payload = {
#         "firstname": "Jim",
#         "lastname": "Brown",
#         "totalprice": 111,
#         "depositpaid": True,
#         "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-10"},
#         "additionalneeds": "Breakfast"
#     }
#
#     created = client.create_booking(booking_payload)
#     print("Created booking:", created)
#
#     booking_id = created.get("bookingid")
#     print("Booking id:", booking_id)
#
#     got = client.get_booking(booking_id)
#     print("Got booking:", got)
#
#     token = client.create_token("admin", "password123")
#     print("Token:", token)
#
#     updated = client.partial_update_booking(booking_id, {"firstname": "James"})
#     print("Updated:", updated)
#
#     deleted = client.delete_booking(booking_id)
#     print("Deleted:", deleted)
#
#     # client.close()
for i in range(1, 10, 3):  # Нечетные числа от 1 до 9
     print(i, end=" ")
