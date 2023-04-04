*Structura proiectului
	Proiectul este format din foldere si fisiere python file:
	  - venv
	  - reports
	  - teste_emag.py
	  - teste_herokuapp.py 
	  - setari_htmltestRunner.py 
	  - main.py 
	  -READ.md.
	
	Pentru inceput avem nevoie sa instalam librariile necesare. 
	Putem folosii comanda pip install -r requirements.txt in terminal sau le putem instala din 
	setarile proiectului.
	   1. In fisierul teste_emag am importat librariile necesare, am creat o clasa
	   si am inceput sa scriu codul pentru fiecare test in parte.
	   2.In fisierul teste_herokuapp am urmat aceeasi pasi ca si la teste_emag,am importat setarile 
	   aferente noului url,si am scris codul noilor teste.
	   3.In setari_htmltestRunner se afla  librariile si setarile de care avem nevoie pentru rularea 
	   suitei de teste (formata din 2 clase).
	   
* Rularea testelor
    -Testele se pot rula individual,sau putem rula o intreaga clasa ori o suita,cu ajutorul butonului 
	 run din stanga testelor.
	-Pentru a genera un raport avem nevoie sa instalam htmltestRunner si sa facem setarile suitei de 
	 teste. 
    -Raportul se va genera la sfarsitul rularii tuturor testelor si va aparea in folderul reports.
		Acesta se poate deschide cu ajutorul oricarui browser.
		
*Functionalitatea testelor:
    -Prin testele create am incercat sa interactionez cu elementele paginilor,si sa testez functionalitatea 
	lor(butoane de logare ,adaugarea si stergerea unor produse din cosul de cumparaturi, etc.).
	-Unele teste ar putea fi nefunctionale pe viitor :
	    - la fiecare logare dupa introducerea datelor se cere un cod trimis automat pe telefon;
	    - ofertele au un anumit termen calendaristic;
	    - majoritatea elementelor pot fi adaugate in cosul de cumparaturi, dar daca dorim sa le stergem sau 
	    sa le mutam la favorite in momentul testarii ,primim fail deoarece este nevoie de logare.
	
    