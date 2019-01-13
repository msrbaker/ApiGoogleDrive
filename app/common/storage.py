from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, \
    GoogleDrivePermissionRole, GoogleDriveFilePermission
from django.conf import settings


if settings.GDRIVE_USER_EMAIL:
    permission = GoogleDriveFilePermission(
        GoogleDrivePermissionRole.READER,
        GoogleDrivePermissionType.USER,
        settings.GDRIVE_USER_EMAIL
    )
else:
    permission = GoogleDriveFilePermission(
        GoogleDrivePermissionRole.READER,
        GoogleDrivePermissionType.ANYONE
    )

gd_storage = GoogleDriveStorage(permissions=(permission, ))
