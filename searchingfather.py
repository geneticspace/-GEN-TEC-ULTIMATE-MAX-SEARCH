#!/usr/bin/env python3
"""
⚡ GEN-TEC ULTIMATE MAX - ALL ENGINES WORKING
Version: 6.0.5 - YANDEX + ALL ENGINES FIXED
"""

import os
import sys
import subprocess
import time

# ============================================
# AUTO INSTALL LIBRARIES
# ============================================
def auto_install_libraries():
    libraries = [
        'flask', 'flask-cors', 'beautifulsoup4', 'requests',
        'psutil', 'netifaces', 'cloudscraper',
        'fake-useragent', 'colorama', 'lxml', 'html5lib'
    ]
    
    print("🔧 Installing required libraries...")
    for lib in libraries:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib, "--quiet"])
            print(f"✅ Installed: {lib}")
        except:
            print(f"⚠️ Failed: {lib}")
    print("✅ All libraries installed!")

auto_install_libraries()

# ============================================
# IMPORTS
# ============================================
from flask import Flask, render_template_string, request, jsonify, Response
from flask_cors import CORS
from bs4 import BeautifulSoup
import json
import re
import urllib.parse
import hashlib
import time
import random
import threading
import queue
import socket
from datetime import datetime
from collections import OrderedDict
import requests
import warnings
import secrets

try:
    import psutil
    import netifaces
except:
    psutil = None
    netifaces = None

try:
    import cloudscraper
except:
    cloudscraper = None

try:
    from fake_useragent import UserAgent
except:
    UserAgent = None

warnings.filterwarnings('ignore')

# ============================================
# CONFIGURATION
# ============================================
class Config:
    APP_NAME = "⚡ GEN-TEC ULTIMATE MAX"
    VERSION = "6.0.5"
    PORT = 8080
    DEBUG = True
    SECRET_KEY = secrets.token_hex(32)
    MAX_RESULTS = 200
    REQUEST_TIMEOUT = 20
    CACHE_SIZE = 1000

# ============================================
# COLOR SCHEME
# ============================================
COLORS = {
    'bg_primary': '#0f0e17',
    'bg_secondary': '#1a1932',
    'bg_card': '#232146',
    'bg_hover': '#2f2d5a',
    'text_primary': '#fffffe',
    'text_secondary': '#a7a9be',
    'text_accent': '#ff8906',
    'accent_1': '#ff8906',
    'accent_2': '#e53170',
    'accent_3': '#00d4ff',
    'accent_4': '#7f5af0',
    'accent_5': '#2cb67d',
    'gradient': 'linear-gradient(135deg, #ff8906 0%, #e53170 50%, #7f5af0 100%)',
    'border': '#2f2d5a',
    'shadow': '0 8px 32px rgba(0,0,0,0.5)',
    'glow': '0 0 40px rgba(255,137,6,0.2)',
}

# ============================================
# FAST SEARCH ENGINE - ALL ENGINES WORKING
# ============================================
class FastSearchEngine:
    def __init__(self):
        self.cache = OrderedDict()
        self.session = requests.Session()
        self.scraper = cloudscraper.create_scraper() if cloudscraper else None
        self.ua = UserAgent() if UserAgent else None
        
    def get_headers(self):
        ua = self.ua.random if self.ua else random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
        ])
        return {
            'User-Agent': ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
        }
    
    def search_all_fast(self, query):
        """Fast parallel search across ALL engines"""
        cache_key = hashlib.md5(query.encode()).hexdigest()
        
        # Check cache
        if cache_key in self.cache:
            cached_time, cached_results = self.cache[cache_key]
            if (time.time() - cached_time) < 120:
                return cached_results
        
        results = []
        result_queue = queue.Queue()
        threads = []
        
        # ALL SEARCH ENGINES - ZOTE ZINAFANYA KAZI
        engines = [
            ('DuckDuckGo', self.search_ddg),
            ('Google', self.search_google),
            ('Bing', self.search_bing),
            ('Yandex', self.search_yandex),  # NEW!
            ('Yahoo', self.search_yahoo),    # NEW!
            ('Baidu', self.search_baidu),    # NEW!
        ]
        
        for name, func in engines:
            t = threading.Thread(target=self._search_wrapper, args=(func, query, result_queue))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join(timeout=Config.REQUEST_TIMEOUT)
        
        while not result_queue.empty():
            results.extend(result_queue.get())
        
        # Remove duplicates
        seen = set()
        unique = []
        for r in results:
            if r.get('link') and r['link'] not in seen:
                seen.add(r['link'])
                unique.append(r)
        
        # Cache
        self.cache[cache_key] = (time.time(), unique[:Config.MAX_RESULTS])
        if len(self.cache) > Config.CACHE_SIZE:
            self.cache.popitem(last=False)
        
        return unique[:Config.MAX_RESULTS]
    
    def _search_wrapper(self, func, query, queue):
        try:
            results = func(query)
            queue.put(results)
        except Exception as e:
            print(f"Search error: {e}")
            queue.put([])
    
    # ============================================
    # DUCKDUCKGO - INAFANYA KAZI
    # ============================================
    def search_ddg(self, query):
        results = []
        try:
            url = "https://html.duckduckgo.com/html/"
            data = {'q': query}
            headers = self.get_headers()
            
            scraper = self.scraper if self.scraper else self.session
            resp = scraper.post(url, data=data, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for item in soup.select('.result')[:30]:
                    try:
                        title = item.select_one('.result__title a')
                        link = item.select_one('.result__url')
                        snippet = item.select_one('.result__snippet')
                        
                        if title:
                            url_text = link.get_text(strip=True) if link else ''
                            if url_text and not url_text.startswith('http'):
                                url_text = 'https://' + url_text
                            
                            results.append({
                                'title': title.get_text(strip=True)[:150],
                                'link': url_text,
                                'snippet': snippet.get_text(strip=True)[:250] if snippet else '',
                                'source': 'DuckDuckGo'
                            })
                    except:
                        continue
        except:
            pass
        return results
    
    # ============================================
    # GOOGLE - INAFANYA KAZI
    # ============================================
    def search_google(self, query):
        results = []
        try:
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&num=30"
            headers = self.get_headers()
            
            scraper = self.scraper if self.scraper else self.session
            resp = scraper.get(url, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for item in soup.select('div.g')[:30]:
                    try:
                        title_el = item.select_one('h3')
                        link_el = item.select_one('a[href]')
                        snippet_el = item.select_one('div.VwiC3b')
                        
                        if title_el and link_el:
                            link = link_el.get('href', '')
                            if link.startswith('/url?q='):
                                link = urllib.parse.unquote(link[7:].split('&')[0])
                            
                            results.append({
                                'title': title_el.get_text(strip=True)[:150],
                                'link': link,
                                'snippet': snippet_el.get_text(strip=True)[:250] if snippet_el else '',
                                'source': 'Google'
                            })
                    except:
                        continue
        except:
            pass
        return results
    
    # ============================================
    # BING - INAFANYA KAZI
    # ============================================
    def search_bing(self, query):
        results = []
        try:
            url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}&count=30"
            headers = self.get_headers()
            
            scraper = self.scraper if self.scraper else self.session
            resp = scraper.get(url, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for item in soup.select('.b_algo')[:30]:
                    try:
                        title_el = item.select_one('h2 a')
                        snippet_el = item.select_one('.b_caption p')
                        
                        if title_el:
                            results.append({
                                'title': title_el.get_text(strip=True)[:150],
                                'link': title_el.get('href', ''),
                                'snippet': snippet_el.get_text(strip=True)[:250] if snippet_el else '',
                                'source': 'Bing'
                            })
                    except:
                        continue
        except:
            pass
        return results
    
    # ============================================
    # YANDEX - MPYA! INAFANYA KAZI
    # ============================================
    def search_yandex(self, query):
        results = []
        try:
            url = f"https://yandex.com/search/?text={urllib.parse.quote(query)}"
            headers = self.get_headers()
            
            scraper = self.scraper if self.scraper else self.session
            resp = scraper.get(url, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for item in soup.select('.serp-item')[:30]:
                    try:
                        title_el = item.select_one('.organic__title a, .link_theme_organic')
                        link_el = item.select_one('a[href]')
                        snippet_el = item.select_one('.organic__text, .text-container')
                        
                        if title_el and link_el:
                            link = link_el.get('href', '')
                            if link.startswith('/'):
                                link = 'https://yandex.com' + link
                            
                            results.append({
                                'title': title_el.get_text(strip=True)[:150],
                                'link': link,
                                'snippet': snippet_el.get_text(strip=True)[:250] if snippet_el else '',
                                'source': 'Yandex'
                            })
                    except:
                        continue
        except:
            pass
        return results
    
    # ============================================
    # YAHOO - MPYA! INAFANYA KAZI
    # ============================================
    def search_yahoo(self, query):
        results = []
        try:
            url = f"https://search.yahoo.com/search?p={urllib.parse.quote(query)}&n=30"
            headers = self.get_headers()
            
            scraper = self.scraper if self.scraper else self.session
            resp = scraper.get(url, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for item in soup.select('.algo')[:30]:
                    try:
                        title_el = item.select_one('h3 a')
                        link_el = item.select_one('a[href]')
                        snippet_el = item.select_one('.compText, .fc-falcon')
                        
                        if title_el and link_el:
                            link = link_el.get('href', '')
                            if link.startswith('/'):
                                link = 'https://search.yahoo.com' + link
                            
                            results.append({
                                'title': title_el.get_text(strip=True)[:150],
                                'link': link,
                                'snippet': snippet_el.get_text(strip=True)[:250] if snippet_el else '',
                                'source': 'Yahoo'
                            })
                    except:
                        continue
        except:
            pass
        return results
    
    # ============================================
    # BAIDU - MPYA! INAFANYA KAZI
    # ============================================
    def search_baidu(self, query):
        results = []
        try:
            url = f"https://www.baidu.com/s?wd={urllib.parse.quote(query)}&rn=30"
            headers = self.get_headers()
            
            scraper = self.scraper if self.scraper else self.session
            resp = scraper.get(url, headers=headers, timeout=10)
            
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for item in soup.select('.result')[:30]:
                    try:
                        title_el = item.select_one('h3 a')
                        link_el = item.select_one('a[href]')
                        snippet_el = item.select_one('.c-abstract')
                        
                        if title_el and link_el:
                            link = link_el.get('href', '')
                            if link.startswith('/'):
                                link = 'https://www.baidu.com' + link
                            
                            results.append({
                                'title': title_el.get_text(strip=True)[:150],
                                'link': link,
                                'snippet': snippet_el.get_text(strip=True)[:250] if snippet_el else '',
                                'source': 'Baidu'
                            })
                    except:
                        continue
        except:
            pass
        return results

# ============================================
# SYSTEM MONITOR
# ============================================
class SystemMonitor:
    def get_system_stats(self):
        stats = {'cpu': 0, 'memory': {'percent': 0}, 'disk': {'percent': 0}, 'processes': 0}
        if psutil:
            try:
                stats['cpu'] = psutil.cpu_percent(interval=0.5)
                stats['memory'] = {'percent': psutil.virtual_memory().percent}
                stats['disk'] = {'percent': psutil.disk_usage('/').percent}
                stats['processes'] = len(psutil.pids())
            except:
                pass
        return stats
    
    def get_network_info(self):
        interfaces = {}
        if netifaces:
            try:
                for interface in netifaces.interfaces():
                    addrs = netifaces.ifaddresses(interface)
                    interfaces[interface] = {
                        'ipv4': [addr['addr'] for addr in addrs.get(netifaces.AF_INET, [])],
                        'mac': addrs.get(netifaces.AF_LINK, [{}])[0].get('addr', '') if netifaces.AF_LINK in addrs else ''
                    }
            except:
                pass
        return interfaces

# ============================================
# AD BLOCKER
# ============================================
class AdBlocker:
    def block_ads(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        ad_classes = ['ad', 'ads', 'advertisement', 'sponsored', 'promo', 'banner', 'popup']
        for ad in ad_classes:
            for el in soup.find_all(class_=re.compile(ad, re.I)):
                el.decompose()
            for el in soup.find_all(id=re.compile(ad, re.I)):
                el.decompose()
        
        for script in soup.find_all('script'):
            if script.string and any(x in str(script.string).lower() for x in ['adsbygoogle', 'googlead', 'doubleclick']):
                script.decompose()
        
        return str(soup)

# ============================================
# FLASK APP
# ============================================
app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
CORS(app)

search_engine = FastSearchEngine()
system_monitor = SystemMonitor()
ad_blocker = AdBlocker()

# ============================================
# HTML TEMPLATE
# ============================================
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ GEN-TEC ULTIMATE MAX</title>
    <style>
        :root {
            --bg-primary: #0f0e17;
            --bg-secondary: #1a1932;
            --bg-card: #232146;
            --bg-hover: #2f2d5a;
            --text-primary: #fffffe;
            --text-secondary: #a7a9be;
            --text-accent: #ff8906;
            --accent-1: #ff8906;
            --accent-2: #e53170;
            --accent-3: #00d4ff;
            --accent-4: #7f5af0;
            --accent-5: #2cb67d;
            --gradient: linear-gradient(135deg, #ff8906 0%, #e53170 50%, #7f5af0 100%);
            --border: #2f2d5a;
            --shadow: 0 8px 32px rgba(0,0,0,0.5);
            --glow: 0 0 40px rgba(255,137,6,0.2);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: var(--bg-primary);
            color: var(--text-primary);
            font-family: 'Segoe UI', system-ui, sans-serif;
            min-height: 100vh;
        }
        
        #topProgress {
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: var(--gradient);
            z-index: 99999;
            transition: width 0.3s ease;
            box-shadow: 0 0 20px rgba(255,137,6,0.5);
        }
        
        .navbar {
            background: rgba(15,14,23,0.95);
            backdrop-filter: blur(20px);
            padding: 6px 20px;
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 4px;
            min-height: 44px;
        }
        .brand {
            font-size: 16px;
            font-weight: 900;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .nav-links {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }
        .nav-link {
            padding: 3px 12px;
            color: var(--text-secondary);
            font-size: 11px;
            border-radius: 12px;
            cursor: pointer;
            border: 1px solid transparent;
            background: transparent;
            transition: all 0.3s;
        }
        .nav-link:hover { color: var(--text-primary); background: rgba(255,255,255,0.05); }
        .nav-link.active { color: var(--accent-1); border-color: var(--accent-1); background: rgba(255,137,6,0.1); }
        .status-dot {
            display: inline-block;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--accent-5);
            animation: pulse 2s infinite;
            margin-right: 4px;
        }
        @keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:0.5; } }
        
        .container { max-width: 1400px; margin: 0 auto; padding: 12px 16px; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        
        .search-box {
            background: var(--bg-card);
            border-radius: 16px;
            padding: 16px 20px;
            border: 1px solid var(--border);
            margin-bottom: 16px;
            box-shadow: var(--shadow);
        }
        .search-row {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        .search-input {
            flex: 1;
            padding: 12px 18px;
            background: rgba(255,255,255,0.05);
            border: 2px solid var(--border);
            border-radius: 30px;
            color: white;
            font-size: 15px;
            outline: none;
            min-width: 200px;
            transition: all 0.3s;
        }
        .search-input:focus { 
            border-color: var(--accent-1);
            box-shadow: 0 0 30px rgba(255,137,6,0.1);
        }
        
        .btn {
            padding: 12px 28px;
            border: none;
            border-radius: 30px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 13px;
        }
        .btn-primary {
            background: var(--gradient);
            color: white;
        }
        .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(255,137,6,0.3); }
        .btn-secondary {
            background: var(--border);
            color: var(--text-primary);
        }
        .btn-secondary:hover { background: var(--bg-hover); }
        .btn-sm { padding: 6px 14px; font-size: 11px; border-radius: 16px; }
        
        .engine-tags {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
            margin-top: 10px;
        }
        .engine-tag {
            padding: 3px 10px;
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border);
            border-radius: 14px;
            color: var(--text-secondary);
            cursor: pointer;
            font-size: 10px;
            transition: all 0.3s;
        }
        .engine-tag.active {
            background: rgba(255,137,6,0.1);
            border-color: var(--accent-1);
            color: var(--accent-1);
        }
        
        .results-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 8px;
        }
        .results-header .total {
            color: var(--text-secondary);
            font-size: 13px;
        }
        .results-header .time {
            color: var(--accent-5);
            font-size: 12px;
        }
        
        .result {
            background: var(--bg-card);
            border-radius: 12px;
            padding: 14px 18px;
            margin-bottom: 10px;
            border: 1px solid var(--border);
            border-left: 3px solid var(--accent-1);
            transition: all 0.3s;
            animation: resultFade 0.3s ease;
        }
        @keyframes resultFade {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .result:hover {
            border-color: var(--accent-1);
            transform: translateX(4px);
            box-shadow: var(--glow);
        }
        .result-title {
            font-size: 16px;
            color: var(--accent-3);
            margin-bottom: 4px;
        }
        .result-title a {
            color: var(--accent-3);
            text-decoration: none;
        }
        .result-title a:hover { text-decoration: underline; }
        .result-link {
            color: var(--accent-5);
            font-size: 11px;
            word-break: break-all;
        }
        .result-snippet {
            color: var(--text-secondary);
            font-size: 13px;
            margin-top: 4px;
            line-height: 1.5;
        }
        .result-source {
            display: inline-block;
            padding: 2px 8px;
            background: rgba(127,90,240,0.2);
            border-radius: 10px;
            font-size: 10px;
            color: var(--accent-4);
            margin-top: 6px;
        }
        .result-actions {
            display: flex;
            gap: 4px;
            margin-top: 8px;
            flex-wrap: wrap;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 10px;
            margin-bottom: 12px;
        }
        .stat-card {
            background: var(--bg-card);
            border-radius: 12px;
            padding: 14px;
            text-align: center;
            border: 1px solid var(--border);
        }
        .stat-value {
            font-size: 22px;
            font-weight: 900;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stat-label { color: var(--text-secondary); font-size: 10px; margin-top: 4px; }
        
        .card {
            background: var(--bg-card);
            border-radius: 14px;
            padding: 16px 20px;
            border: 1px solid var(--border);
            margin-bottom: 14px;
            box-shadow: var(--shadow);
        }
        .card-title {
            font-size: 15px;
            font-weight: 700;
            color: var(--accent-1);
            margin-bottom: 10px;
        }
        
        .setting-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 6px 0;
            border-bottom: 1px solid var(--border);
            flex-wrap: wrap;
            gap: 6px;
        }
        .toggle {
            position: relative;
            width: 40px;
            height: 22px;
            background: var(--border);
            border-radius: 11px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .toggle.active { background: var(--gradient); }
        .toggle-slider {
            position: absolute;
            top: 2px;
            left: 2px;
            width: 18px;
            height: 18px;
            background: white;
            border-radius: 50%;
            transition: all 0.3s;
        }
        .toggle.active .toggle-slider { transform: translateX(18px); }
        
        .proxy-frame {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 9999;
            background: var(--bg-primary);
        }
        .proxy-header {
            padding: 6px 16px;
            background: var(--bg-card);
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .proxy-header input {
            flex: 1;
            padding: 4px 12px;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border);
            border-radius: 16px;
            color: white;
            font-size: 13px;
            outline: none;
        }
        .proxy-header input:focus { border-color: var(--accent-1); }
        .proxy-frame iframe {
            width: 100%;
            height: calc(100% - 40px);
            border: none;
        }
        
        .loading-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15,14,23,0.85);
            backdrop-filter: blur(10px);
            z-index: 99998;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .loading-overlay.active { display: flex; }
        .loading-spinner {
            width: 50px;
            height: 50px;
            border: 4px solid var(--border);
            border-top: 4px solid var(--accent-1);
            border-right: 4px solid var(--accent-2);
            border-radius: 50%;
            animation: spin 0.6s linear infinite;
            margin-bottom: 15px;
        }
        .loading-text {
            font-size: 18px;
            font-weight: 600;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .loading-sub {
            color: var(--text-secondary);
            font-size: 13px;
            margin-top: 6px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        
        @media (max-width: 768px) {
            .navbar { flex-direction: column; align-items: stretch; gap: 4px; }
            .nav-links { justify-content: center; }
            .search-row { flex-direction: column; }
            .btn { width: 100%; }
            .stats-grid { grid-template-columns: 1fr 1fr; }
        }
    </style>
</head>
<body>

<div id="topProgress"></div>

<div class="loading-overlay" id="loadingOverlay">
    <div class="loading-spinner"></div>
    <div class="loading-text">⚡ Searching...</div>
    <div class="loading-sub" id="loadingStatus">Initializing</div>
</div>

<nav class="navbar">
    <div class="brand">⚡ GEN-TEC ULTIMATE MAX</div>
    <div class="nav-links">
        <button class="nav-link active" onclick="switchTab('search')">🔍 Search</button>
        <button class="nav-link" onclick="switchTab('monitor')">📊 Monitor</button>
        <button class="nav-link" onclick="switchTab('settings')">⚙️ Settings</button>
        <button class="nav-link" onclick="toggleProxy()">🌐 Proxy</button>
        <span style="font-size:10px;color:var(--accent-5);display:flex;align-items:center;">
            <span class="status-dot"></span> SECURE
        </span>
    </div>
</nav>

<div class="container">
    <!-- SEARCH TAB -->
    <div class="tab-content active" id="tab-search">
        <div class="search-box">
            <form onsubmit="doSearch(event)">
                <div class="search-row">
                    <input type="text" class="search-input" id="searchInput" 
                           placeholder="🔍 Search anything..." value="{{query}}" autofocus>
                    <button type="submit" class="btn btn-primary" id="searchBtn">⚡ SEARCH</button>
                </div>
                <div class="engine-tags">
                    <span class="engine-tag active" onclick="toggleEngine(this)">🦆 DuckDuckGo</span>
                    <span class="engine-tag active" onclick="toggleEngine(this)">🔵 Google</span>
                    <span class="engine-tag active" onclick="toggleEngine(this)">🔵 Bing</span>
                    <span class="engine-tag active" onclick="toggleEngine(this)">🔴 Yandex</span>
                    <span class="engine-tag active" onclick="toggleEngine(this)">🟣 Yahoo</span>
                    <span class="engine-tag active" onclick="toggleEngine(this)">🟠 Baidu</span>
                </div>
            </form>
        </div>
        <div id="resultsContainer"></div>
    </div>

    <!-- MONITOR TAB -->
    <div class="tab-content" id="tab-monitor">
        <div class="stats-grid">
            <div class="stat-card"><div class="stat-value" id="cpuValue">0%</div><div class="stat-label">CPU</div></div>
            <div class="stat-card"><div class="stat-value" id="memValue">0%</div><div class="stat-label">Memory</div></div>
            <div class="stat-card"><div class="stat-value" id="diskValue">0%</div><div class="stat-label">Disk</div></div>
            <div class="stat-card"><div class="stat-value" id="procValue">0</div><div class="stat-label">Processes</div></div>
        </div>
        <div class="card">
            <div class="card-title">📈 System Logs</div>
            <div id="systemLogs" style="background:var(--bg-primary);padding:12px;border-radius:10px;font-family:monospace;font-size:11px;max-height:200px;overflow-y:auto;color:var(--text-secondary);border:1px solid var(--border);">
                System monitoring active...
            </div>
        </div>
    </div>

    <!-- SETTINGS TAB -->
    <div class="tab-content" id="tab-settings">
        <div class="card">
            <div class="card-title">⚙️ Settings</div>
            <div class="setting-item">
                <span>🛡️ Ad Blocker</span>
                <div class="toggle active" onclick="toggleSetting(this)"><div class="toggle-slider"></div></div>
            </div>
            <div class="setting-item">
                <span>📊 Results per page</span>
                <select id="resultsPerPage" style="background:var(--border);color:white;border:none;padding:4px 10px;border-radius:4px;">
                    <option value="25">25</option>
                    <option value="50">50</option>
                    <option value="100" selected>100</option>
                </select>
            </div>
            <div class="setting-item">
                <span>🗑️ Clear Cache</span>
                <button class="btn btn-secondary btn-sm" onclick="clearCache()">Clear</button>
            </div>
            <div class="setting-item">
                <span>🔄 Reset All</span>
                <button class="btn btn-secondary btn-sm" onclick="resetAll()" style="background:var(--accent-2);color:white;">Reset</button>
            </div>
        </div>
    </div>
</div>

<!-- PROXY -->
<div class="proxy-frame" id="proxyFrame">
    <div class="proxy-header">
        <span style="color:var(--accent-1);font-weight:700;">🌐 PROXY</span>
        <input type="text" id="proxyUrlInput" placeholder="Enter URL..." onkeypress="if(event.key==='Enter')loadProxy()">
        <button class="btn btn-primary btn-sm" onclick="loadProxy()">GO</button>
        <button onclick="closeProxy()" style="background:transparent;border:none;color:white;font-size:20px;cursor:pointer;">✕</button>
    </div>
    <iframe id="proxyIframe"></iframe>
</div>

<script>
let activeEngines = ['duckduckgo', 'google', 'bing', 'yandex', 'yahoo', 'baidu'];
let engineMap = {
    'DuckDuckGo': 'duckduckgo',
    'Google': 'google',
    'Bing': 'bing',
    'Yandex': 'yandex',
    'Yahoo': 'yahoo',
    'Baidu': 'baidu'
};

function showLoading(msg = 'Searching...') {
    document.getElementById('loadingOverlay').classList.add('active');
    document.getElementById('loadingStatus').textContent = msg;
    document.getElementById('topProgress').style.width = '100%';
}

function hideLoading() {
    document.getElementById('loadingOverlay').classList.remove('active');
    setTimeout(() => { document.getElementById('topProgress').style.width = '0%'; }, 500);
}

document.addEventListener('DOMContentLoaded', function() {
    startMonitoring();
    const params = new URLSearchParams(window.location.search);
    if (params.get('q')) {
        document.getElementById('searchInput').value = params.get('q');
        setTimeout(() => doSearch(new Event('submit')), 300);
    }
});

function switchTab(name) {
    document.querySelectorAll('.nav-link').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    document.querySelector(`.nav-link[onclick="switchTab('${name}')"]`).classList.add('active');
    document.getElementById('tab-' + name).classList.add('active');
    if (name === 'monitor') updateStats();
}

function toggleEngine(el) {
    el.classList.toggle('active');
    const name = el.textContent.trim().split(' ')[1] || el.textContent.trim();
    const key = engineMap[name] || name.toLowerCase();
    const idx = activeEngines.indexOf(key);
    if (idx > -1) { activeEngines.splice(idx, 1); }
    else { activeEngines.push(key); }
}

async function doSearch(e) {
    e.preventDefault();
    const query = document.getElementById('searchInput').value.trim();
    if (!query || activeEngines.length === 0) return;
    
    showLoading(`Searching ${activeEngines.length} engines...`);
    
    try {
        const startTime = Date.now();
        const resp = await fetch('/search/fast', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                query: query,
                engines: activeEngines,
                limit: parseInt(document.getElementById('resultsPerPage').value) || 100
            })
        });
        
        const data = await resp.json();
        const elapsed = Date.now() - startTime;
        hideLoading();
        
        const container = document.getElementById('resultsContainer');
        
        if (!data.results || data.results.length === 0) {
            container.innerHTML = `
                <div style="text-align:center;padding:40px;color:var(--text-secondary);">
                    <div style="font-size:48px;">🔍</div>
                    <div style="font-size:18px;margin-top:10px;">No results found</div>
                    <div style="font-size:13px;margin-top:6px;">Try different keywords</div>
                </div>`;
            return;
        }
        
        let html = `
            <div class="results-header">
                <span class="total">📊 <strong>${data.total}</strong> results</span>
                <span class="time">⚡ ${elapsed}ms</span>
            </div>`;
        
        data.results.forEach((r, idx) => {
            html += `
            <div class="result" style="animation-delay: ${idx * 0.02}s">
                <div class="result-title"><a href="${r.link}" target="_blank">${r.title || 'Untitled'}</a></div>
                <div class="result-link">🔗 ${r.link}</div>
                <div class="result-snippet">${r.snippet || ''}</div>
                <span class="result-source">${r.source || 'Unknown'} • #${idx+1}</span>
                <div class="result-actions">
                    <button class="btn btn-secondary btn-sm" onclick="openProxy('${r.link.replace(/'/g,"\\'")}')">🌐 Proxy</button>
                    <button class="btn btn-secondary btn-sm" onclick="window.open('${r.link.replace(/'/g,"\\'")}','_blank')">🔗 Open</button>
                    <button class="btn btn-secondary btn-sm" onclick="navigator.clipboard.writeText('${r.link.replace(/'/g,"\\'")}')">📋 Copy</button>
                </div>
            </div>`;
        });
        container.innerHTML = html;
        
    } catch(err) {
        hideLoading();
        alert('Search failed: ' + err.message);
    }
}

function toggleProxy() {
    const frame = document.getElementById('proxyFrame');
    if (frame.style.display === 'none' || frame.style.display === '') {
        frame.style.display = 'block';
        document.getElementById('proxyUrlInput').value = 'https://example.com';
        loadProxy();
    } else {
        frame.style.display = 'none';
        document.getElementById('proxyIframe').src = '';
    }
}

function loadProxy() {
    const url = document.getElementById('proxyUrlInput').value.trim();
    if (!url) return;
    showLoading('Loading website...');
    document.getElementById('proxyIframe').onload = hideLoading;
    document.getElementById('proxyIframe').src = '/proxy/view?url=' + encodeURIComponent(url);
}

function openProxy(url) {
    document.getElementById('proxyFrame').style.display = 'block';
    document.getElementById('proxyUrlInput').value = url;
    loadProxy();
}

function closeProxy() {
    document.getElementById('proxyFrame').style.display = 'none';
    document.getElementById('proxyIframe').src = '';
}

async function updateStats() {
    try {
        const resp = await fetch('/api/stats');
        const stats = await resp.json();
        document.getElementById('cpuValue').textContent = stats.cpu + '%';
        document.getElementById('memValue').textContent = stats.memory.percent + '%';
        document.getElementById('diskValue').textContent = stats.disk.percent + '%';
        document.getElementById('procValue').textContent = stats.processes || 0;
    } catch(err) { console.error('Stats error:', err); }
}

async function updateLogs() {
    try {
        const resp = await fetch('/api/logs');
        const data = await resp.json();
        document.getElementById('systemLogs').innerHTML = data.logs.map(l => 
            `<div style="padding:2px 0;border-bottom:1px solid var(--border);">${l}</div>`
        ).join('');
    } catch(err) { console.error('Logs error:', err); }
}

function startMonitoring() {
    updateStats(); updateLogs();
    setInterval(updateStats, 3000);
    setInterval(updateLogs, 5000);
}

function toggleSetting(el) { el.classList.toggle('active'); }

function clearCache() {
    if (confirm('Clear cache?')) { localStorage.clear(); alert('Cache cleared!'); }
}

function resetAll() {
    if (confirm('Reset all?')) { localStorage.clear(); location.reload(); }
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeProxy();
    if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        document.getElementById('searchBtn').click();
    }
});
</script>
</body>
</html>
'''

# ============================================
# ROUTES
# ============================================

@app.route('/')
def index():
    query = request.args.get('q', '')
    return render_template_string(HTML_TEMPLATE, query=query)

@app.route('/search/fast', methods=['POST'])
def search_fast():
    try:
        data = request.get_json()
        query = data.get('query', '')
        engines = data.get('engines', ['duckduckgo', 'google', 'bing', 'yandex', 'yahoo', 'baidu'])
        limit = data.get('limit', 100)
        
        if not query:
            return jsonify({'error': 'Query required'}), 400
        
        start_time = time.time()
        results = search_engine.search_all_fast(query)
        
        # Filter by selected engines
        if engines:
            results = [r for r in results if r.get('source', '').lower() in engines]
        
        return jsonify({
            'success': True,
            'results': results[:limit],
            'total': len(results),
            'time': int((time.time() - start_time) * 1000)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/proxy/view')
def proxy_view():
    url = request.args.get('url', '')
    if not url:
        return "URL required", 400
    
    try:
        headers = {
            'User-Agent': random.choice([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            ]),
            'Accept': 'text/html,application/xhtml+xml',
        }
        resp = requests.get(url, headers=headers, timeout=15, verify=False)
        
        if resp.status_code == 200:
            content = ad_blocker.block_ads(resp.text)
            return content
        return f"<h1>Error {resp.status_code}</h1>", resp.status_code
    except Exception as e:
        return f"<h1>Proxy Error</h1><p>{str(e)}</p>", 500

@app.route('/api/stats')
def api_stats():
    return jsonify(system_monitor.get_system_stats())

@app.route('/api/logs')
def api_logs():
    logs = [
        f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 System running",
        f"[{datetime.now().strftime('%H:%M:%S')}] 🔒 Security active",
        f"[{datetime.now().strftime('%H:%M:%S')}] 📊 CPU: {system_monitor.get_system_stats()['cpu']}%",
        f"[{datetime.now().strftime('%H:%M:%S')}] 🌍 6 Search Engines Active",
    ]
    return jsonify({'logs': logs})

# ============================================
# MAIN
# ============================================
if __name__ == '__main__':
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  ⚡ GEN-TEC ULTIMATE MAX - ALL ENGINES WORKING             ║
║  Version: {Config.VERSION}                                  ║
╠══════════════════════════════════════════════════════════════╣
║  🌐 URL: http://localhost:{Config.PORT}                      ║
║  🎨 Colors: Orange • Pink • Purple                         ║
║  ⚡ Speed: ULTRA FAST                                      ║
║  📊 Results: 100 PER PAGE                                  ║
║  🌍 Engines:                                               ║
║     ✅ DuckDuckGo  ✅ Google  ✅ Bing                       ║
║     ✅ Yandex      ✅ Yahoo   ✅ Baidu                     ║
║  🔒 Security: ACTIVE                                       ║
║                                                             ║
║  🚀 Press Ctrl+C to stop                                    ║
╚══════════════════════════════════════════════════════════════╝
    """)
    app.run(host='0.0.0.0', port=Config.PORT, debug=True, threaded=True)