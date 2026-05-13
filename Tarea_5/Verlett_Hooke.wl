VerletResorte[x0_, v0_, dt_, Ns_] := Module[
  {positions, xPrev, xCur, xNext, t, k = 1.0, m = 1.0},
  
  (* Inicializamos la tabla de resultados {tiempo, posicion} *)
  positions = Table[{0.0, 0.0}, {i, 1, Ns}];
  
  (* Condiciones iniciales *)
  xCur = x0;
  
  (* Usamos Euler hacia atrás o v0 para encontrar la posición anterior *)
  xPrev = x0 - v0*dt + 0.5*(-k/m*x0)*dt^2;
  
  positions[[1]] = {0.0, x0};
  
  (* Bucle de integración *)
  For[index = 2, index <= Ns, index++,
    
    t = (index - 1)*dt;
    
    (* aceleración *)
    xNext = 2*xCur - xPrev + (-k/m*xCur)*dt^2;
    
    (* Actualización *)
    xPrev = xCur;
    xCur = xNext;
    
    positions[[index]] = {t, xCur};
  ];
  
  Return[positions];
]

(* Ejecutar simulación *)
datos = VerletResorte[1.0, 0.0, 0.1, 100];

(* Crear gráfica *)
grafica = ListLinePlot[
  datos,
  PlotStyle -> Red,
  AxesLabel -> {"Tiempo", "Posición"},
  PlotLabel -> "Método de Verlet - Resorte Hookiano"
];

(* Exportar imagen *)
Export["verlet.png", grafica];
