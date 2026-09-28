import time
class RateLimiter:
    def __init__(self, token_capacity, refill_rate_per_sec):
        self.capacity = token_capacity
        self.refill_rate = refill_rate_per_sec
        self.ledger = {}
    def allow_request(self, client_ip):
        now = time.time()
        if client_ip not in self.ledger:
            self.ledger[client_ip] = {"tokens": self.capacity, "last_updated": now}
        state = self.ledger[client_ip]
        elapsed = now - state["last_updated"]
        state["tokens"] = min(self.capacity, state["tokens"] + (elapsed * 
self.refill_rate))
        state["last_updated"] = now
        if state["tokens"] >= 1:
            state["tokens"] -= 1
            return True
        return False
# Local orchestration check simulating rapid requests
limiter = RateLimiter(token_capacity=3, refill_rate_per_sec=0.5)
client_ip = "192.168.1.10"

for i in range(6):
    result = limiter.allow_request(client_ip)

    if result:
        print(f"Request {i + 1}: ALLOWED")
    else:
        print(f"Request {i + 1}: BLOCKED")
