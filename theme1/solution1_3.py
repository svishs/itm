if __name__ == "__main__":
    A = 34
    print(f"{A=} A больше нуля? {A>0}")
    print(f"{A=} А является нечетным? {A%2!=0}")
    print(f"{A=} A является четным? {A%2==0}")
    # 4. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3».
    A, B = 3, 5
    print(f" {A=} {B=} . Справедливы неравенства A > 2 и B ≤ 3 {(A>2)and(B<=3)}")
    # 5. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥ 0 или B < −2».
    print(f" {A=} {B=} .Справедливы неравенства A ≥ 0 или B < −2 ? {(A>=0)or(B<-2)}")
    # 6. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < C».
    C = 15
    print(f" {A=} {B=} {C=}. Справедливо двойное неравенство A < B < C {A<B<C}")
    # 7. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и C».
    print(f" {A=} {B=} {C=}. Число B находится между числами A и C {A<B<C}")
    # 8. Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».
    print(f" {A=} {B=} . Каждое из чисел A и B нечетное? {A%2!=0 and B%2!=0}")
    # 9. Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».
    print(f" {A=} {B=} . Хотя бы одно из чисел A и B нечетное? {A%2!=0 or B%2!=0} ")
    # 10. Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное» V
    print(f" {A=} {B=} . Ровно одно из чисел A и B нечетное? {A%2!=0 ^ B%2!=0}")
