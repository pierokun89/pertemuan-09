#latihan prtemuan 9
print(3*'=','tugas pertemuan 9','='*3)
print('| Nama\t: Nur hidayat\t|\n| NIM\t: 312110584\t|\n| Kelas\t: TI.21.C5\t|')
print(25*'=','\n')
a = [6, 7, 8, 9, 10]                                                        #buat list sebanyak 5 elemen
print(" a = [6, 7, 8, 9, 10]\n")          

print(8*'=','akses',8*'=') 
print('elemen ke 3 adalah', a[2])                                           # tampilkan elemen ke 3 ,
del a[1:4]                                                                  # ambil elemen ke 2-4
print('setelah elemen 2 sampai 4 diambil maka menjadi',a)                                                              
del a[1]                                                                    # ambil elemen terakhir
print('setelah elemen terakhir diambil maka menjadi',a,"\n")                                                              

print(8*'=','ubah',8*'=')                                                      
a = [6, 7, 8, 9, 10]                                                        
a [3] =  5                                                                  #ubah elemen ke 4 dengan nilainya , 
print('setelah merubah elemen ke-4 maka menjadi', a)
a [3:5] = 3, 4                                                              #ubah elemen ke 4- terakhir
print('setelah merubah elemen ke-4 sampai terakhir maka menjadi', a,'\n')
print(8*'=','tambah',8*'=')
a = [6, 7, 8, 9, 10] 
b = []
b.extend (a[0:2])                                                           #ambil 2 bagian dari list pertama (a) dan jadikan list ke 2 B
print ('hasil setelah mengambil 2 bagian elemen a maka b=', b)
b.append('delapan')                                                         #- tambah list b dengan nilai string
print('setelah menambah string pada elemen b hasilnya', b)
b.extend([9, 10, 11])                                                       #- tambah list b dengan 3 nilai
print('setelah menambah 3 bilai menjadi', b)
c=a+b                                                                       #- gabungkan list b dan list a
print('hasil penggabungan list a dan b hasilnya',c)