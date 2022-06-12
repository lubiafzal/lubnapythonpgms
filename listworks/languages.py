frameworks=[
    ["django","python",4],
    ["flask","python",3],
    ["spring","java",5],
    ["express","javascript",4],
    ["angular","type_script",4]
]


java=print([fw for fw in frameworks if fw[1]=="java"])
python=print([fw for fw in frameworks if fw[1]=="python"])
popular=print([fw for fw in frameworks if fw[-1]>3])
