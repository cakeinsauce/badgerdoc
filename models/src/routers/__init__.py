from tenant_dependency import get_tenant_info

from src.constants import ALGORITHM, KEYCLOACK_URI

tenant = get_tenant_info(url=KEYCLOACK_URI, algorithm=ALGORITHM)
