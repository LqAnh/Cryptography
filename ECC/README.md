> points.py file calculate all points in elliptic curves

+ p, a, b need to be defined to run the program

    - `p` , `a`, `b`: y^2 = x^3 + `a`x + `b` mod `p`





> add.py file calculate sum of two point in elliptic curves

+ P, Q, num, prime, a, b need to be defined to run the program

    - eg: `P` = [1, 2]
    - `Q` = [3, 4] if you want to add P to itself then `Q = P`
    - `num` : number of time you want to calculate P `start from 2`
        -  eg: calculate 2P => num = 3
        -  P + Q => num = 3
        -  3P => num = 4
        -  4P => num = 5
    - `prime`, `a`, `b`: y^2 = x^3 + `a`x + `b` mod `prime`