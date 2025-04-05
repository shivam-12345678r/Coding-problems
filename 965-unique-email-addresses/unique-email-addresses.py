class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local,domain = email.split('@')
            local =  local.split('+')[0].replace('.','')
            normal = f"{local}@{domain}"
            unique.add(normal)
        return len(unique)
        