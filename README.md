# Matkasuunnitelmasovellus

## Sovelluksen toiminnot

- Sovelluksessa käyttäjät pystyvät jakamaan matkasuunnitelmiaan. Matkasuunnitelmassa lukee matkakohde, matkan ajankohta ja listaus matkan aktiviteeteista.
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään matkasuunnitelmia sekä muokkaamaan ja poistamaan omia matkasuunnitelmiaan.
- Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät matkasuunnitelmat.
- Käyttäjä pystyy etsimään matkasuunnitelmia hakusanalla (esim. “Japani”).
- Sovelluksessa on käyttäjäsivut, jotka näyttävät, montako matkasuunnitelmaa käyttäjä on lisännyt sekä listan käyttäjän lisäämistä matkasuunnitelmista.
- Käyttäjä pystyy valitsemaan matkasuunnitelmalle yhden tai useamman luokittelun (esim. kaupunkiloma, rantaloma tai luontokohde).
- Käyttäjä pystyy antamaan matkasuunnitelmalle kommentin (esim. vinkkejä matkasuunnitelman parantamiseen). Matkasuunnitelmassa näytetään siihen lisätyt kommentit.

## Sovelluksen asennus

Asenna `flask` -kirjasto

```
$ pip install flask
```

Luo tietokannan taulut 

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Käynnistä ohjelma komennolla

```
$ flask run
```