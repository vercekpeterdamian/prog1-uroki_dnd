# prog1-uroki_dnd
Za predmet Programiranje 1 in lastno uporabo bom zbral in preučil uroke v igri Dungeons and Dragons, ki so dosegljivi na [te spletni strani](http://dnd5e.wikidot.com/spells).

Trenutno sem naredil le zahtevane `.csv` datoteke. Commit je pa žal le en, saj programa ni prav dosti in je zelo hitro prešel iz *ne deluje* na *deluje*.

## Kaj vsebujejo datoteke?
`podatki/uroki.csv` vsebuje večino podatkov o urokih:
 - **urok_href**: niz vstavimo `f'http://dnd5e.wikidot.com/spells:{ime}'` in bomo odpeljani na spletno stran z več podatki o uroku
 - **urok**: Ime uroka
 - **sola**: število, ki "razkodiramo" s pomočjo `sola.csv`
 - **urocanje**: število, ki "razkodiramo" s pomočjo `urocanje.csv`. Pove nam koliko časa se urok izvaja.
 - **doseg**: stevilo, ki ga "razkodiramo" s pomočjo `doseg.csv`
 - **efekt**: ..., pove nam koliko časa urok traja po izvedbi
 - **ritual**: nam pove, če je možno urok izvesti kot ritual
 - **verbal, somatic, material**: kaj okvirno potrebujemo za izvedbo uroka
 - **stopnja**: katere stopnje je urok. Št. 0 ustreza Cantripu.

Ostale datoteke najdene v `podatki/` so bodisi `.json`, ki so verjetno nepotrebne, bodisi zgoraj omenjene.
