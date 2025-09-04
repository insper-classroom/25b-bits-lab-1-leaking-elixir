# -*- coding: utf-8 -*-
"""Exercice 1

Implemente a equacão:

q = a or !b
"""


from myhdl import *


@block
def exe1(q, a, b):
    """
    q = a or !b
    """

    @always_comb
    def comb():
        q.next = a or (not b)
        pass

    return instances()


@block
def exe2(q, a, b, c):
    """
    Implemente a tabela verdade a seguir:

    A B C | Q
    ------|--
    0 0 0 | 1
    0 0 1 | 0
    0 1 0 | 0
    0 1 1 | 1
    1 0 0 | 1
    1 0 1 | 0
    1 1 0 | 0
    1 1 1 | 1

    Não utilize IF!
    """

    @always_comb
    def comb():
<<<<<<< HEAD
        q.next = (not (b or c)) or b and c 
=======
        q.next = (not (b or c)) or b and c
>>>>>>> f2a95fbff65b9d5dc3487ada400c09ddf80590a8

    return instances()


@block
def exe3(q, a, b, c, d, e):
    """
    Exercice 3

    Implemente o circuito lógico a seguir:

               __
    a---------\  \
              |   )-  __
    b---------/__/  -|  \
                     |   )-
    c----------------|__/  -  __
                            -|  \
                             |   )-
    d------------------------|__/  -  __
                                    -|  \
                                     |   )-----
    e--------------------------------|__/
    """

    @always_comb
    def comb():
<<<<<<< HEAD
        q.next = (a or b) and c and d and e
=======
        q.next = (a or b) and c and d and e 
>>>>>>> f2a95fbff65b9d5dc3487ada400c09ddf80590a8

    return instances()


@block
def exe4(led, sw):
    """
    led0 é sw[0] and (não sw[1])
    """

    @always_comb
    def comb():
        led[0].next = sw[0] and (not sw[1])

    return instances()


@block
def exe5(leds, sw):
    """
    led0 é uma copia da chave sw0
    led1 é sw0 & sw1
    led2 é o led1 invertido
    led3 é xor entre sw0 e sw1
    todos os outros leds acesos
    """

    @always_comb
    def comb():
<<<<<<< HEAD
        leds[0].next = sw[0]
        leds[1].next = sw[0] and sw[1]
        leds[2].next = (not leds[1])
        leds[3].next =  sw[0]^sw[1]
        leds[4].next = 1
        leds[5].next = 1
        leds[6].next = 1
        leds[7].next = 1
        leds[8].next = 1 
        leds[9].next = 1
        pass

=======
        led[0] = sw[0]
        led[1] = sw[0] and sw[1]
        led[2] = (not led[1])
        led[3] =  sw[0]^sw[1]
        led[4] = 1
        led[5] = 1
        led[6] = 1
        led[7] = 1
        led[8] = 1 
        led[9] = 1
>>>>>>> f2a95fbff65b9d5dc3487ada400c09ddf80590a8
    return instances()


@block
def sw2hex(hex_pins, sw):
    """
    Faz a conversão de binário para display de 7 segmentos
    """

    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex_pins.next = "1000000"
        elif sw[4:0] == 1:
            hex_pins.next = "1111001"
        elif sw[4:0] == 2:
            hex_pins.next = "1000000"
        elif sw[4:0] == 3:
            hex_pins.next = "1000000"
        elif sw[4:0] == 4:
            hex_pins.next = "1000000"
        elif sw[4:0] == 5:
            hex_pins.next = "1000000"
        elif sw[4:0] == 6:
            hex_pins.next = "1000000"
        elif sw[4:0] == 7:
            hex_pins.next = "1000000"
        elif sw[4:0] == 8:
            hex_pins.next = "1000000"
        elif sw[4:0] == 9:
            hex_pins.next = "1000000"
        elif sw[4:0] == 10:
            hex_pins.next = "1000000"
        elif sw[4:0] == 11:
            hex_pins.next = "1000000"
        elif sw[4:0] == 12:
            hex_pins.next = "1000000"
        elif sw[4:0] == 13:
            hex_pins.next = "1000000"
        elif sw[4:0] == 14:
            hex_pins.next = "1000000"
        else:
            hex_pins.next = "1000000"

    return instances()
