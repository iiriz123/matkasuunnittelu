# Matkasuunnitelmasovellus

## Sovelluksen toiminnot tällä hetkellä

- Sovelluksessa käyttäjät pystyvät jakamaan matkasuunnitelmiaan. Matkasuunnitelmassa lukee matkakohde, matkan alkamisajankohta (päättymisajankohta kehitteillä) ja listaus matkan aktiviteeteista
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään matkasuunnitelmia sekä muokkaamaan ja poistamaan omia matkasuunnitelmiaan.
- Käyttäjä näkee sovellukseen lisätyt matkasuunnitelmat. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät matkasuunnitelmat.
- Käyttäjä pystyy etsimään matkasuunnitelmia hakusanalla (esim. “Japani”).

## Kehitettävät toiminnot

- Käyttäjäsivu näyttää, montako matkasuunnitelmaa käyttäjä on lisännyt sekä listan käyttäjän lisäämistä matkasuunnitelmista.
- Käyttäjä pystyy valitsemaan matkasuunnitelmalle yhden tai useamman luokittelun (esim. kaupunkiloma, rantaloma tai luontomatka).
- Käyttäjä pystyy antamaan matkasuunnitelmalle kommentin (esim. vinkkejä matkasuunnitelman parantamiseen). Matkasuunnitelmassa näytetään siihen lisätyt kommentit.

## Sovelluksen asennus

Asenna `flask` -kirjasto

```
$ pip install flask
```

Luo tietokannan taulut 

```
$ sqlite3 database.db < schema.sql
```

Käynnistä ohjelma komennolla

```
$ flask run
```