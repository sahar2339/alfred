from datetime import datetime



def time_passed_since_created(time_passed: str) -> int:
    created_at = time_passed
    created_at = created_at.replace('Z', '').replace('T','')
    created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    time_passed = (datetime.now() - created_at).total_seconds()
    return time_passed

