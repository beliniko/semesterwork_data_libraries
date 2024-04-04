from github import Github

# Erstellen Sie ein Github-Objekt mit Ihrem Zugriffstoken
g1 = Github("xxx")
g2 = Github("xxx")

# Abrufen des Ratenbegrenzungsstatus
rate_limit1 = g1.get_rate_limit()
core_rate1 = rate_limit1.core

rate_limit2 = g2.get_rate_limit()
core_rate2 = rate_limit2.core

# Anzeigen der verbleibenden und maximalen Anzahl von Anfragen
print(core_rate1.remaining, core_rate1.limit)
print(core_rate2.remaining, core_rate2.limit)

# Zeitpunkt des Zurücksetzens des Ratenlimits
reset_time = core_rate1.reset
print(f"Das Ratenlimit wird zurückgesetzt um: {reset_time}")