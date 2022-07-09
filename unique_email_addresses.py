class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        sendableEmails = {}

        for email in emails:
            reducedEmail = self.reduceEmail(email)
            if reducedEmail == "":
                continue
            sendableEmails[reducedEmail] = True

        return len(sendableEmails)


    def reduceEmail(self, email: str) -> str:
        emailParts = email.split("@")
        localParts, domain = emailParts[0].replace(".", ""), emailParts[1]
        local = localParts.split("+")[0]

        domainParts = domain.split(".")

        if len(emailParts) > 2:
            return ""

        for char in domain:
            if not char.isalpha() and char != "." and char != "+":
                return ""

        if domainParts[-1] != "com":
            return ""

        for char in local:
            if not char.isalpha():
                return ""

        return local + "@" + domain


emails = [
    "fg.r.u.uzj+o.pw@kziczvh.com",
    "r.cyo.g+d.h+b.ja@tgsg.z.com",
    "fg.r.u.uzj+o.f.d@kziczvh.com",
    "r.cyo.g+ng.r.iq@tgsg.z.com",
    "fg.r.u.uzj+lp.k@kziczvh.com",
    "r.cyo.g+n.h.e+n.g@tgsg.z.com",
    "fg.r.u.uzj+k+p.j@kziczvh.com",
    "fg.r.u.uzj+w.y+b@kziczvh.com",
    "r.cyo.g+x+d.c+f.t@tgsg.z.com",
    "r.cyo.g+x+t.y.l.i@tgsg.z.com",
    "r.cyo.g+brxxi@tgsg.z.com",
    "r.cyo.g+z+dr.k.u@tgsg.z.com",
    "r.cyo.g+d+l.c.n+g@tgsg.z.com",
    "fg.r.u.uzj+vq.o@kziczvh.com",
    "fg.r.u.uzj+uzq@kziczvh.com",
    "fg.r.u.uzj+mvz@kziczvh.com",
    "fg.r.u.uzj+taj@kziczvh.com",
    "fg.r.u.uzj+fek@kziczvh.com"
]

emails2 = ["linqmafia@leet+code.com","linqmafia@code.com"]
s = Solution()
print(s.numUniqueEmails(emails)) #=> 2
print(s.numUniqueEmails(emails2)) #=> 2
