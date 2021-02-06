						LACEMENT du projet
- pour lancer le projet, il suffit de lancer la commande make, cela éxecute le fichier Makefile
-à la fin de l'éxecution, un fichier de données "strat.dat" contient les résultats des stratégies pour différents packets sous la forme :
	numero_de_packet;numero_de_la_strategie
-une image "plot.png" est généré aussi, elle contient le graphe représentant les données dans le fichier "strat.dat", cela est généré
avec le code "code_plot.pg".
structure des fichiers :
	-"code_plot.gp" : code qui permet d'avoir un graphe 
	-"functions_calcul.py" : fichiers avec les fonctions de calcul
	-"Packet.py" : contient la classe packet
	-"Trame.py" : contient la classe trame
	-"main.py" : main généré
	-"strat.dat" : fichier de données
 
