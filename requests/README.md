### Proxies
If you need to use a proxy, you can configure individual requests with the proxies argument to any request method:
```
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
requests.get('http://example.org', proxies=proxies)

```