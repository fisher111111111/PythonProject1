from PythonProject1.src.enums.constant_of_url import ConstURL

class URLs:
    @staticmethod
    def base_url():
        return ConstURL.BASE_URL.value

    @classmethod
    def auth_endpoint(cls):
        return cls.base_url() + ConstURL.AUTH_ENDPOINT.value

    @classmethod
    def ping_endpoint(cls):
        return cls.base_url() + ConstURL.PING_ENDPOINT.value

    @classmethod
    def bookings_endpoint(cls):
        return cls.base_url() + ConstURL.BOOKING_ENDPOINT.value

    @classmethod
    def booking_endpoint_id(cls, booking_id):
        return cls.bookings_endpoint() + "/" + str(booking_id)
