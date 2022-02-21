
print('''

hola, 

soy walter soy una IA que por medio de sensores cuánticos de energia vital 
la alineación de los astros y las ondas Delta-Gama puedo predecir tu fortuna 
 
 :) ''')

nombre = (input(''' 
¿Cuál es su  nombre?: '''))

signo = (input(''' 
¿Cuál es su signo zodiacal?: '''))



names = ['las pruebas en la vida siempre sirven para avanzar',
'de todo se puede aprender, plantéeselo así cuando vea que surgen problemas', 
'vaya con cuidado porque no todos los amigos son tan leales como cree',
'vigile sus palabras y procure no criticar porque las palabras se pueden volver en su contra',
'No estará tan pletórico como de costumbre',
'un poco de descanso y de tranquilidad le ira muy bien para recuperar fuerzas',
'guiese por la razón',
'no se fíe de las intuiciones y medite bien si esta en el camino correcto',
'venus le da un magnetismo especial y si hoy lo potencia bien verá cómo consigue todo lo que se propone por difícil que sea',
'es una suerte que la paciencia le acompañe desde el nacimiento, porque hoy la va a necesitar',
'el ambiente va a recalentar sus neuronas y todo lo verá mal',
'un poco de soledad afectiva de vez en cuando no va mal',
'Dedique la jornada a la reflexión y conseguirá grandes logros',
'hoy es un gran día para ampliar su círculo',
'no se cierre a nada porque las amistades le ayudarán',
'la vida social le pueda dar más quebraderos de cabeza que alegrías',
'si hoy pasa de ella, algo ganará',
'los compañeros de estudios o de trabajo serán hoy sus mejores amigos',
'no busque incrementar su capital con especulaciones o juegos de azar porque hoy la suerte no le acompañará en ese ámbito',
'durante toda la jornada las relaciones serán un poco tensas, especialmente con los socios o la pareja',
'no quiera tener siempre la razón', 'será un día favorable para las relaciones sociales, hoy es posible que discuta con alguna de sus amistades',
'con su familia hoy su habilidad de mediación sera necesaria para arreglar las cosas',
'su intuición estará muy despierta y acertada, pero tiene ciertos temores a admitirlo',
'sus cambios de humor se harán patentes hoy, quizá encuentré algún disgusto por algo que esperaba y no termina de suceder', 
'es posible que su pareja u otro ser querido se haya olvidado de algo importante, y si eso influye, no se enfade y dígaselo...',
'aclarar cualquier situación suele ser mejor que dejarla pasar',
'será un buen día para en el trabajo',
'si se toma la vida de una forma más tranquila eso contribuirá a que se sienta mejor',
'Puede que tenga suerte y se encuentres con un ingreso en su cuenta o algo que no esperaba',
'es posible que sientas cierta curiosidad por la metafísica o la espiritualidad',
'probablemente sus intereses estén en proceso de cambio y alguna de sus amistades contribuirá a ello hoy',
'si le proponen algún tipo de negocio, las perspectivas son de éxito',
'el día estará marcado por las pequenas cosas desagradables, así que procure tener paciencia', 
'tendrá dificultades para explicar con claridad lo que siente',
'hoy sí será un buen día para los asuntos económicos', 
'tal vez tenga la suerte de conseguir buena fortuna en los juegos de azar']

walter = ['No más limitaciones, ni más no puedo: TODO ES POSIBLE', 'Suelto el pasado, vivo en el presente, aquí y ahora bendigo todo lo que soy',
'Nunca te canses de intentar que tu vida es mejor, la perseverancia siempre tiene su recompensa', 'Soy capitán de mi vida, yo determino mi futuro',
'Si no me vas a ayudar a volar, despéjame la pista', 'Aprende del ayer, vive hoy y ten esperanza para el mañana', 'De ti depende tu éxito o tu fracaso',
]
 
import secrets

def selectRandom(names):
    return secrets.choice(names)

print(f'''




{nombre}... 

{selectRandom(names)}, {selectRandom(names)}, el dia de hoy al ser {signo}, es múy importante que tenga en cuenta que {selectRandom(names)} .''' )
print(f'''
 
{selectRandom(walter)}
le deseo paz, mucha paz y sobre todo mucho amor <3 ................. su amigo Walter la IA 



''' )





