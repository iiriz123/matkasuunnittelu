# Matkasuunnitelmasovellus

Matkasuunnittelu on verkkosovellus, jossa käyttäjät pystyvät jakamaan matkasuunnitelmiaan ja jakamaan vinkkejä/kommentteja muiden käyttäjien suunnitelmiin. Matkasuunnitelmissa lukee matkakohde, matkan ajankohta ja listaus matkan aktiviteeteista. Lisäksi käyttäjä pystyy valitsemaan matkasuunnitelmalle yhden tai useamman luokittelun (matkakohde: kaupunkiloma, rantaloma jne.; budjetti: keskihintainen, luksus jne.).

## Sovelluksen keskeiset toiminnot

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään matkasuunnitelmia sekä muokkaamaan ja poistamaan omia matkasuunnitelmiaan.
- Matkasuunnitelmaan voi halutessaan myös lisätä yhden tai useamman kuvan. Kuvia voi myös poistaa.
- Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät matkasuunnitelmat.
- Käyttäjä pystyy etsimään matkasuunnitelmia hakusanalla.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät, montako matkasuunnitelmaa käyttäjä on lisännyt sekä listan käyttäjän lisäämistä matkasuunnitelmista.
- Käyttäjä pystyy antamaan matkasuunnitelmalle kommentin (esim. vinkkejä matkasuunnitelman parantamiseen). Matkasuunnitelmassa näytetään siihen lisätyt kommentit.

## Sovelluksen asennus

### Kloonaa repositorio

```
git clone https://github.com/iiriz123/matkasuunnittelu.git
```

### Siirry hakemistoon

```
cd matkasuunnittelu
```

### Luo ja aktivoi virtuaaliympäristö

```
python3 -m venv venv
```

```
source venv/bin/activate
```

### Asenna `flask` -kirjasto

```
pip install flask
```

### Luo tietokannan taulut ja lisää alkutiedot

```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```

### Käynnistä sovellus komennolla

```
flask run
```

## Sovelluksen toiminta suurella tietomäärällä

Suuri määrä testidataa luotiin `seed.py` tiedoston avulla, joka luo

- tuhat käyttäjää
- sata tuhatta arvostelua
- miljoona kommenttia

Testataan ensin ilman sivutusta tai indeksejä:
Ladataan etusivu, valitaan yksi matkasuunnitelmista, palataan etusivulle.
Etusivun lataaminen vie lähes 2s. Eli aivan liian kauan.

```
elapsed time: 1.86 s
127.0.0.1 - - [28/Feb/2026 13:49:07] "GET / HTTP/1.1" 200 -
elapsed time: 0.05 s
127.0.0.1 - - [28/Feb/2026 13:49:14] "GET /item/100000 HTTP/1.1" 200 -
elapsed time: 1.8 s
127.0.0.1 - - [28/Feb/2026 13:49:19] "GET / HTTP/1.1" 200 -
```

Etusivun latausta saatiin hieman nopeutettua lisäämällä siihen sivutus, jolloin etusivu näyttää kymmenen arvostelua kerralla. Alla kolmen ensimmäisen sivun läpi selaaminen pelkällä sivutuksella:

```
elapsed time: 1.18 s
127.0.0.1 - - [28/Feb/2026 14:32:59] "GET / HTTP/1.1" 200 -
elapsed time: 1.13 s
127.0.0.1 - - [28/Feb/2026 14:33:05] "GET /2 HTTP/1.1" 200 -
elapsed time: 1.21 s
127.0.0.1 - - [28/Feb/2026 14:33:19] "GET /3 HTTP/1.1" 200 -
```

Sivutus ei kuitenkaan pelkästään riitä parantamaan käyttökokemusta.
Tietokanta kokoaa yhteen tietoa tauluista items ja comments, mikä hidastaa tällä hetkellä sovelluksen sivujen lataamista, koska kommenttien yhdistäminen matkasuunnitelmiin id-numeron perusteella on epätehokasta. Jotta sivujen latausta voidaan nopeuttaa, lisättiin kommenttitauluun indeksointi:

```
CREATE INDEX idx_item_comments ON comments (item_id);
```

Tällöin etusivun lataaminen ja sivun vaihto on noin sata kertaa nopeampaa:

```
elapsed time: 0.03 s
127.0.0.1 - - [28/Feb/2026 16:28:05] "GET / HTTP/1.1" 200 -
elapsed time: 0.01 s
127.0.0.1 - - [28/Feb/2026 16:28:30] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.01 s
127.0.0.1 - - [28/Feb/2026 16:28:33] "GET /3 HTTP/1.1" 200 -
```
