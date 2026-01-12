**README.md**  
<br><br>

I denna labb anropas ett API för att hämta en token, utföra ett token‑exchange och därefter få ut en flagga.
<br>
Scriptet hämtar tre API:er i snabb följd genom POST i en uppsatt tailscale-miljö.
<br><br>

/ = http://10.3.10.104:3000
<br>
/api/token - Create a short-lived token
<br>
/api/verify - Verify a token
<br>
/api/flag - Exchange verified token for a flag
<br><br><br>

  
Scriptet måste köras i snabb följd p.g.a. en tidsbegränsning för inhämtning på servern.

**Scriptet är uppdelad i två delar av definition (def).**

    * Första delen skickar in POST från andra delen - endpoint, headers etc. tar emot nyckelvärde och felhanterar.

    * Andra delen består av POST-variablerna. Dessa är uppdelade i:

        - endpoint_url ex. api/token

        - nyckel:nyckelvärde

        - Plain text
<br><br><br>
  

1) Version 1 (getok-v1.py)A innehåller inga definitioner
2) Version 2 (getok-v2.py) innehåller definitioner, något mer lättläst?
3) Version 3 (getok-v3.py) Innehåller definitioner, något mer svårläst? men 23 rader kortare än v.2.
<br><br><br>


CLI Lazies:
<br><br>
Requirements:

```

pip install -r requirements.txt

```


<br>
Latest version exec:

```

python getok-v3.py

```

<br><br><br>
Källinformation kan inhämtas på http://10.3.10.104:3000/docs
