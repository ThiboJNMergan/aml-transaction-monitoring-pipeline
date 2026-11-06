# Data dictionary



## HI-Small_Trans.csv

Dit is een lijst van alle overschrijvingen tussen alle rekeningen in de gesimuleerde wereld, over een periode van enkele weken.

| Kolom | Type | Betekenis | Opmerking |
|---|---|---|---|
| Timestamp | TIMESTAMP | Datum en tijdstip van de transactie | Op de minuut nauwkeurig |
| From Bank | VARCHAR | Code van de bank van de verzender | Tekst, want in de csv staan voorloopnullen (bv. `010`) |
| Account | VARCHAR | Rekeningnummer van de verzender | |
| To Bank | VARCHAR | Code van de bank van de ontvanger | Zelfde opmerking als From Bank |
| Account_1 | VARCHAR | Rekeningnummer van de ontvanger | Heet in de csv ook `Account`. DuckDB hernoemt de tweede automatisch |
| Amount Received | DOUBLE | Bedrag dat de ontvanger krijgt | In Receiving Currency |
| Receiving Currency | VARCHAR | Valuta waarin ontvangen wordt | bv. US Dollar, Euro, Bitcoin |
| Amount Paid | DOUBLE | Bedrag dat de verzender betaalt | In Payment Currency |
| Payment Currency | VARCHAR | Valuta waarin betaald wordt | Verschilt van Receiving Currency als er omgewisseld wordt |
| Payment Format | VARCHAR | Betaalmethode | bv. ACH, Wire, Cheque, Cash, Credit Card, Bitcoin, Reinvestment |
| Is Laundering | BIGINT | 1 = witwassen, 0 = gewone transactie | Het "antwoord" waarop je regels getest worden |

Een rekening is uniek door de combinatie bank + rekeningnummer.

## HI-Small_accounts.csv

Een lijst van alle rekeningen, met welke bank en wie de eigenaar is. Eén rij zegt: rekening X bij Bank A is van Corporation #1234.

| Kolom | Type | Betekenis | Opmerking |
|---|---|---|---|
| Bank Name | VARCHAR | Naam van de bank | |
| Bank ID | BIGINT | Code van de bank | Getal, dus zonder voorloopnullen |
| Account Number | VARCHAR | Rekeningnummer | |
| Entity ID | VARCHAR | ID van de eigenaar van de rekening | Eén eigenaar kan meerdere rekeningen hebben |
| Entity Name | VARCHAR | Soort eigenaar met volgnummer | bv. Corporation, Sole Proprietorship, Partnership |

## Koppeling tussen de twee tabellen

| Trans | Accounts |
|---|---|
| From Bank + Account | Bank ID + Account Number (verzender) |
| To Bank + Account_1 | Bank ID + Account Number (ontvanger) |

Let op: `From Bank` / `To Bank` zijn tekst, `Bank ID` is een getal. Bij een JOIN moet je één van beide omzetten naar het type van de andere, anders foutmelding 

## HI-Small_Patterns.txt

```
BEGIN LAUNDERING ATTEMPT - FAN-OUT
<transacties, zelfde kolommen als Trans maar zonder kopregel>
END LAUNDERING ATTEMPT - FAN-OUT
```

Soorten patronen:

| Patroon | Wat er gebeurt |
|---|---|
| FAN-OUT | Eén rekening stuurt naar veel rekeningen |
| FAN-IN | Veel rekeningen sturen naar één rekening |
| CYCLE | Geld gaat via een kring van rekeningen terug naar het begin |
| SCATTER-GATHER | Geld wordt verspreid en daarna weer verzameld bij één rekening |
| GATHER-SCATTER | Geld wordt verzameld en daarna weer verspreid |
| STACK | Lagen van rekeningen die geld doorgeven |
| BIPARTITE | Een groep rekeningen stuurt naar een andere groep |
| RANDOM | Geld gaat langs willekeurige rekeningen |

