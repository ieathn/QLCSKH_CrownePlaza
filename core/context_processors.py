# QLCSKH_LTW/core/context_processors.py

def user_roles_processor(request):
    is_user_true_admin = False  # Phân biệt admin thật sự (superuser hoặc loai_tk='admin')
    is_regular_staff_role = False  # Nhân viên thường, không phải admin/superuser

    if request.user.is_authenticated:
        # is_admin function của bạn: user.is_superuser or getattr(user, 'loai_tk', None) == 'admin'
        if request.user.is_superuser or getattr(request.user, 'loai_tk', None) == 'admin':
            is_user_true_admin = True

        if getattr(request.user, 'loai_tk', None) == 'nhan_vien' and not is_user_true_admin:
            is_regular_staff_role = True

    return {
        'is_user_true_admin': is_user_true_admin,
        'is_regular_staff_role': is_regular_staff_role,
    }