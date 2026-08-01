
from django.contrib import admin
from .models import Phong, DichVu, KhachHang, NhanVien, LichLamViec, DonDatPhong, DonDatDichVu, YeuCau, HoaDon

# Đăng ký các model của bạn ở đây
admin.site.register(Phong)
admin.site.register(DichVu)
admin.site.register(KhachHang)
admin.site.register(NhanVien)
admin.site.register(LichLamViec)
admin.site.register(DonDatPhong)
admin.site.register(DonDatDichVu)
admin.site.register(YeuCau)
admin.site.register(HoaDon)