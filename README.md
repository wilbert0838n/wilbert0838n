<!-- ============ HEADER ============ -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1b27,50:24283b,100:7aa2f7&height=200&section=header&text=Wilbert%20Nadar&fontSize=52&fontColor=c0caf5&fontAlignY=38&desc=systems%20%C2%B7%20infra%20%C2%B7%20competitive%20programming&descSize=16&descAlignY=58&descAlign=50&animation=fadeIn" />

<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=900&color=7AA2F7&center=true&vCenter=true&width=620&lines=I+build+judges+that+run+untrusted+code+safely.;Docker+sandboxes+%C2%B7+seccomp+%C2%B7+container+pools;600%2B+problems+solved%2C+still+counting;ICPC+Asia+West+%C2%B7+Chennai+Site" alt="Typing SVG" />
</a>

<br/><br/>

<a href="https://wilbertprojects.me"><img src="https://img.shields.io/badge/ComputeX-live-7aa2f7?style=for-the-badge&labelColor=1a1b27&logo=vercel&logoColor=7aa2f7"/></a>
<a href="https://linkedin.com/in/wilbert-nadar"><img src="https://img.shields.io/badge/LinkedIn-connect-bb9af7?style=for-the-badge&labelColor=1a1b27&logo=linkedin&logoColor=bb9af7"/></a>
<a href="mailto:rohannadar88@gmail.com"><img src="https://img.shields.io/badge/Mail-say_hi-f7768e?style=for-the-badge&labelColor=1a1b27&logo=gmail&logoColor=f7768e"/></a>

</div>

<br/>

<!-- ============ ABOUT ============ -->
<table>
<tr>
<td width="55%" valign="top">

```java
public final class Wilbert extends Engineer {

    String   location   = "Mumbai, IN";
    String   studying   = "Computer Engineering @ TSEC (2028)";
    String   role       = "Core Team @ TSEC CodeCell";

    String[] building   = { "ComputeX", "Rooted" };
    String[] obsessedBy = { "sandboxing", "schedulers",
                            "low-latency judging", "Linux internals" };

    String   now        = "Prepping for ICPC with team W Coders";
    String   funFact    = "600+ problems and still can't stop";
}
```

</td>
<td width="45%" valign="top">

**⚡ quick facts**

🧠 &nbsp;Solo-built a full online judge, sandbox to scoreboard<br/>
🏁 &nbsp;Ran an 8-week national CP league on it, **600+ participants**<br/>
🏆 &nbsp;CodeChef global rank **#297**<br/>
🎯 &nbsp;ICPC Chennai regionals, 2025 and 2026<br/>
✍️ &nbsp;Problem setter for CodeCell contests<br/>
🐳 &nbsp;Currently poking at containerd internals

</td>
</tr>
</table>

<!-- ============ FEATURED ============ -->
<h2 align="center">🚀 featured work</h2>

<table>
<tr>
<td width="50%" valign="top">

### ComputeX
*A competitive programming platform, built entirely solo.*

- Docker-sandboxed execution hardened with a custom **seccomp BPF** profile
- **Prewarmed container pools** for low-latency judging
- **RabbitMQ** queue for async submission handling
- Special-judge checkers, stress-tested problem bank
- Powered CodeCell's Weekly Challenges league

<code>Java 21</code> <code>Spring Boot 3</code> <code>React 18</code> <code>Monaco</code> <code>Docker</code> <code>PostgreSQL</code>

<a href="https://wilbertprojects.me"><img src="https://img.shields.io/badge/try_it-wilbertprojects.me-7aa2f7?style=flat-square&labelColor=1a1b27"/></a>

</td>
<td width="50%" valign="top">

### Rooted
*Container-based hosting for Indian engineering students.*

- Give every student a real Linux box without a real Linux box
- System containers via **sysbox-runc**, so users get Docker-in-container without privileged mode
- Built on the same isolation ideas that run the ComputeX judge

<code>Docker</code> <code>sysbox</code> <code>Linux</code> <code>Nginx</code>

<img src="https://img.shields.io/badge/status-building-e0af68?style=flat-square&labelColor=1a1b27"/>

</td>
</tr>
</table>

<details>
<summary><b>🔍 how a ComputeX submission gets judged</b></summary>
<br/>

```mermaid
flowchart LR
    A[React + Monaco] -->|submit| B[Spring Boot API]
    B -->|enqueue| C[(RabbitMQ)]
    C --> D[Judge Worker]
    D -->|lease| E[Warm Container Pool]
    E -->|seccomp sandbox| F[Compile + Run]
    F --> G[Output Validator / Checker]
    G -->|verdict| H[(PostgreSQL)]
    H --> A
```

</details>

<!-- ============ STACK ============ -->
<h2 align="center">🛠 toolbox</h2>

<div align="center">

<img src="https://skillicons.dev/icons?i=java,cpp,ts,python,go&theme=dark" /><br/><br/>
<img src="https://skillicons.dev/icons?i=spring,rabbitmq,fastapi,react,tailwind&theme=dark" /><br/><br/>
<img src="https://skillicons.dev/icons?i=docker,linux,nginx,gcp,vercel,postgres,supabase&theme=dark" />

</div>

<!-- ============ CP ============ -->
<h2 align="center">⚔️ competitive programming</h2>

<div align="center">

<a href="https://codeforces.com/profile/wilbert0838n"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcodeforces.com%2Fapi%2Fuser.info%3Fhandles%3Dwilbert0838n&query=%24.result%5B0%5D.rating&label=Codeforces&style=for-the-badge&logo=codeforces&logoColor=white&labelColor=1a1b27&color=1F8ACB"/></a>
<a href="https://www.codechef.com/users/wilbert0838n"><img src="https://img.shields.io/badge/CodeChef-Global_%23297-f7768e?style=for-the-badge&logo=codechef&logoColor=white&labelColor=1a1b27"/></a>
<a href="https://leetcode.com/u/wilbert0838n"><img src="https://img.shields.io/badge/LeetCode-600%2B_solved-FFA116?style=for-the-badge&logo=leetcode&logoColor=black&labelColor=1a1b27"/></a>
<a href="https://atcoder.jp/users/wilbert0838n"><img src="https://img.shields.io/badge/AtCoder-wilbert0838n-c0caf5?style=for-the-badge&labelColor=1a1b27"/></a>

<br/><br/>

<img src="https://leetcard.jacoblin.cool/wilbert0838n?theme=dark&font=JetBrains%20Mono&ext=contest&border=0&radius=10" width="60%"/>

</div>

<!-- ============ STATS ============ -->
<h2 align="center">📊 github</h2>

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=wilbert0838n&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github&bg_color=1a1b27&border_radius=10" height="165"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=wilbert0838n&layout=compact&theme=tokyonight&hide_border=true&bg_color=1a1b27&border_radius=10&langs_count=6" height="165"/>

<img src="https://streak-stats.demolab.com?user=wilbert0838n&theme=tokyonight&hide_border=true&background=1a1b27&border_radius=10" width="70%"/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=wilbert0838n&theme=tokyo-night&hide_border=true&bg_color=1a1b27&area=true&radius=10" width="100%"/>

<img src="https://raw.githubusercontent.com/wilbert0838n/wilbert0838n/output/github-contribution-grid-snake-dark.svg" alt="snake eating my contributions" width="100%"/>

</div>

<!-- ============ FOOTER ============ -->
<div align="center">

<br/>

<i>"Make it work, make it right, make it fast."</i>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=wilbert0838n&style=flat-square&color=7aa2f7&label=profile+views"/>

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,50:24283b,100:1a1b27&height=110&section=footer"/>
