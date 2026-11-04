# -*- coding: utf-8 -*-
"""
Межотраслевой баланс Леонтьева.
Пример решения из учебного пособия Габидуллиной З.Р.
«Математические модели логистики», Задача 2, вариант а) (с. 18–23).

Программа повторяет ход решения из пособия и печатает все промежуточные
расчёты в том же порядке и в том же виде, а в конце выполняет проверку.

Числа выводятся с 6 знаками после запятой (как в пособии), лишние нули
отбрасываются (0.300000 -> 0.3). Внутри программа считает без округлений,
поэтому в 6-м знаке возможны расхождения с пособием: авторы при ручном
счёте округляли промежуточные значения.

Запуск:  python mob_primer_zadacha2a.py
Нужен только стандартный Python 3 (без сторонних библиотек).
"""
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = 3
EPS = 1e-9


# ----------------------------------------------------------------------------
# Вспомогательные функции: форматирование и действия с матрицами
# ----------------------------------------------------------------------------
def fm(v, d=6):
    """Число как в пособии: 6 знаков, без хвостовых нулей."""
    if abs(v) < 0.5 * 10 ** (-d):
        v = 0.0
    s = f"{v:.{d}f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def fp(v, d=6):
    """Число для записи внутри произведения: отрицательное берём в скобки."""
    s = fm(v, d)
    return f"({s})" if s.startswith("-") else s


def matrix_lines(M):
    """Матрица в круглых скобках (как в пособии)."""
    cols = [[fm(M[i][j]) for i in range(len(M))] for j in range(len(M[0]))]
    w = [max(len(x) for x in c) for c in cols]
    rows = []
    for i in range(len(M)):
        body = "  ".join(cols[j][i].ljust(w[j]) for j in range(len(M[0])))
        if len(M) == 1:
            l, r = "(", ")"
        elif i == 0:
            l, r = "⎛", "⎞"
        elif i == len(M) - 1:
            l, r = "⎝", "⎠"
        else:
            l, r = "⎜", "⎟"
        rows.append(f"{l} {body} {r}")
    return rows


def column(v):
    return [[x] for x in v]


def show(*parts, gap=" "):
    """Печать в одну «строку» нескольких блоков: текста и матриц.
    Текст (str) выравнивается по средней строке, матрицы (list) — рисуются."""
    blocks = []
    for p in parts:
        if isinstance(p, str):
            blocks.append([p])
        else:
            blocks.append(matrix_lines(p))
    h = max(len(b) for b in blocks)
    out = [""] * h
    for b in blocks:
        width = max(len(s) for s in b)
        top = (h - len(b)) // 2
        for k in range(h):
            s = b[k - top] if 0 <= k - top < len(b) else ""
            out[k] += s.ljust(width) + gap
    for s in out:
        print(s.rstrip())


def matmul(P, Q):
    return [[sum(P[i][k] * Q[k][j] for k in range(len(Q))) for j in range(len(Q[0]))]
            for i in range(len(P))]


def matvec(P, v):
    return [sum(P[i][k] * v[k] for k in range(len(v))) for i in range(len(P))]


def vecmat(v, P):
    return [sum(v[k] * P[k][j] for k in range(len(v))) for j in range(len(P[0]))]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def sub(P, Q):
    return [[P[i][j] - Q[i][j] for j in range(len(P[0]))] for i in range(len(P))]


def transpose(P):
    return [list(r) for r in zip(*P)]


def check_line(name, left, right):
    ok = abs(left - right) < 1e-6
    print(f"  {name}: {fm(left)} = {fm(right)}   "
          f"(разность {left - right:.1e}) -> {'верно' if ok else 'ОШИБКА'}")
    return ok


# ----------------------------------------------------------------------------
# Исходные данные Задачи 2а (с. 18)
# ----------------------------------------------------------------------------
xij = [[65, 35, 0],
       [25, 25, 35],
       [15, 45, 45]]          # межотраслевые потоки, млрд руб.
Y = [65, 65, 75]              # конечный продукт, млрд руб.
Xt = [3300, 2550, 3600]       # трудовые ресурсы, тыс. чел.
Fonds = [100, 120, 150]       # основные производственные фонды, млрд руб.
dY_percent = [40, 10, 40]     # ∆y1 = 40%, ∆y2 = 10%, ∆y3 = 40%

print("=" * 78)
print("Задача 2 а)  (Габидуллина З.Р. «Математические модели логистики», с. 18)")
print("=" * 78)
print("Решение:")
print("В данной задаче даны:")
print("   1) Межотраслевые потоки – (x_ij)3x3")
show("   (x_ij)3x3 =", xij)
print("   2) Вектор конечного продукта")
show("   Y =", column(Y))
print("   3) Затраты живого труда в j –той отрасли x_j^t")
for j in range(N):
    print(f"   x{j + 1}^t = {fm(Xt[j])} (тыс. чел.)")

# --- валовой продукт ---
print("   Вычислим коэффициенты прямых материальных затрат по формуле (8).")
print("Для этого нам нужно знать вектор валового продукта по отраслям:")
X = [sum(xij[i]) + Y[i] for i in range(N)]
for i in range(N):
    terms = " + ".join(fm(v) for v in xij[i])
    print(f"   x{i + 1} = Σ(j=1..n) x{i + 1}j + y{i + 1} = {terms} + {fm(Y[i])} = {fm(X[i])}")

# --- коэффициенты прямых материальных затрат ---
print("Тогда коэффициенты прямых материальных затрат равны:")
A = [[xij[i][j] / X[j] for j in range(N)] for i in range(N)]
for i in range(N):
    parts = []
    for j in range(N):
        if xij[i][j] == 0:
            parts.append(f"a{i + 1}{j + 1} = 0")
        else:
            parts.append(f"a{i + 1}{j + 1} = {fm(xij[i][j])}/{fm(X[j])} = {fm(A[i][j])}")
    print("   " + "    ".join(parts))
show("   (a_ij)3x3 =", A)

# --- E - A ---
E = eye(N)
M = sub(E, A)
print("Вычислим сначала")
show("   E − A =", E, "−", A, "=")
show("   =", M, ".")

# --- алгебраические дополнения ---
print("   Далее вычислим алгебраические дополнения к элементам матрицы Е-А:")
print()
D = [[0.0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        r = [k for k in range(N) if k != i]
        c = [k for k in range(N) if k != j]
        p, q, s, u = M[r[0]][c[0]], M[r[0]][c[1]], M[r[1]][c[0]], M[r[1]][c[1]]
        minor = p * u - q * s
        D[i][j] = (-1) ** (i + j) * minor
        print(f"D{i + 1}{j + 1}=(-1)^{i + j + 2}·({fp(p)}·{fp(u)} - {fp(q)}·{fp(s)}) = {fm(D[i][j])},")

# --- определитель (правило треугольников) ---
m = M
det = (m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[1][0] * m[2][1] * m[0][2]
       - m[0][2] * m[1][1] * m[2][0] - m[0][1] * m[1][0] * m[2][2] - m[1][2] * m[2][1] * m[0][0])
print("Определитель матрицы равен:")
print(f" det(E-A) = {fp(m[0][0])}·{fp(m[1][1])}·{fp(m[2][2])} + {fp(m[0][1])}·{fp(m[1][2])}·{fp(m[2][0])} + "
      f"{fp(m[1][0])}·{fp(m[2][1])}·{fp(m[0][2])} -")
print(f" - {fp(m[0][2])}·{fp(m[1][1])}·{fp(m[2][0])} - {fp(m[0][1])}·{fp(m[1][0])}·{fp(m[2][2])} - "
      f"{fp(m[1][2])}·{fp(m[2][1])}·{fp(m[0][0])} = {fm(det)}.")
det_check = sum(M[0][j] * D[0][j] for j in range(N))  # разложение по 1-й строке
print()

# --- обратная матрица ---
print("Тогда обратная матрица может быть вычислена по формуле (12):")
show("   (E-A)^-1 =", f"1/{fm(det)} ·", D, "^T =")
show("   =", f"1/{fm(det)} ·", transpose(D), ".")
print("После соответствующих вычислений, получаем матрицу (Е-А)^-1:")
B = [[D[j][i] / det for j in range(N)] for i in range(N)]
show("   (E-A)^-1 =", B, ".")

# --- матрица полных материальных затрат ---
print("   Матрица коэффициентов полных материальных затрат может быть")
print("вычислена по формуле (11). Итак, матрица полных материальных затрат равна:")
print("                         С=(Е-А)^-1 - Е.")
C = sub(B, E)
show("   C=(E-A)^-1 − E =", B, "−", E, "=")
show("   =", C, ".")

# --- косвенные затраты 1-го порядка ---
print("   Коэффициенты косвенных материальных затрат 1-го порядка могут")
print("быть вычислены по формуле:")
print("        a_ij^(1) = a_i1·a_1j + a_i2·a_2j + ... + a_in·a_nj ,")
A2 = matmul(A, A)
show("   A^(1) = (a_ij^(1))nxn = A^2 = A×A =", A2, ".")

# --- прямая трудоёмкость ---
print("   Коэффициенты прямых затрат труда на единицу продукции j-той от-")
print("расли определяются по формуле (9):")
t = [Xt[j] / X[j] for j in range(N)]
for j in range(N):
    end = "" if j == N - 1 else ","
    print(f"   t{j + 1} = x{j + 1}^t / x{j + 1} = {fm(Xt[j])} тыс. чел. / {fm(X[j])} млрд. руб. = "
          f"{fm(t[j])} тыс. чел./млрд. руб.{end}")

# --- полная трудоёмкость ---
print("По формуле (11) найдем коэффициенты полной трудоемкости Т:")
T = vecmat(t, B)
show("   T = t·(E-A)^-1 =", [t], "·", B, "=")
print(f"   = ({', '.join(fm(v) for v in T)}).")

# --- изменение валового выпуска ---
dY = [Y[i] * dY_percent[i] / 100 for i in range(N)]
print("Определим величину изменения валового выпуска продукции отрас-")
print("лей")
dX = matvec(B, dY)
show("   ∆x = (E-A)^-1 · ∆y =", B, "·", column(dY), "=", column(dX), ".")

# --- дополнительная потребность в трудовых ресурсах ---
print("Дополнительную потребность в трудовых ресурсах определим следу-")
print("ющим образом:")
dL = [t[j] * dX[j] for j in range(N)]
for j in range(N):
    print(f"   ∆x{j + 1}^t = t{j + 1}·∆x{j + 1} ,  ∆x{j + 1}^t = {fm(t[j])} тыс. чел./млрд. руб. · "
          f"{fm(dX[j])} млрд. руб. = {fm(dL[j])} тыс. чел.")

# --- прямая и полная фондоёмкость ---
print("Вычислим коэффициенты прямой и полной фондоемкости:")
f = [Fonds[j] / X[j] for j in range(N)]
for j in range(N):
    end = "." if j == N - 1 else ","
    print(f"   f{j + 1} = Ф{j + 1} / x{j + 1} = {fm(Fonds[j])} млрд. руб. / {fm(X[j])} млрд. руб. = {fm(f[j])}{end}")
Fc = vecmat(f, B)
show("   F = f·(E-A)^-1 =", [f], "·", B, "=")
print(f"   = ({', '.join(fm(v) for v in Fc)}).")

# --- дополнительная потребность в ОПФ ---
print("Наконец, вычислим дополнительную потребность в основных произ-")
print("водственных фондах:")
dF = [f[j] * dX[j] for j in range(N)]
for j in range(N):
    print(f"   ∆Ф{j + 1} = f{j + 1}·∆x{j + 1} ,  ∆Ф{j + 1} = {fm(f[j])} · {fm(dX[j])} млрд. руб. = "
          f"{fm(dF[j])} млрд. руб.")

# ----------------------------------------------------------------------------
# ПРОВЕРКА
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("ПРОВЕРКА")
print("=" * 78)
ok = True
print("1) (E-A)·(E-A)^-1 = E:")
P = matmul(M, B)
show("   (E-A)·(E-A)^-1 =", P)
ok &= all(abs(P[i][j] - E[i][j]) < 1e-9 for i in range(N) for j in range(N))
print("2) Определитель разложением по 1-й строке: det = Σ m1j·D1j")
ok &= check_line("det(E-A)", det_check, det)
print("3) Основное балансовое соотношение X = A·X + Y:")
AXY = [a + y for a, y in zip(matvec(A, X), Y)]
for i in range(N):
    ok &= check_line(f"x{i + 1}", X[i], AXY[i])
print("4) X = (E-A)^-1·Y (валовой выпуск восстанавливается по конечному продукту):")
BY = matvec(B, Y)
for i in range(N):
    ok &= check_line(f"x{i + 1}", BY[i], X[i])
print("5) ∆X = A·∆X + ∆Y:")
r = [a + y for a, y in zip(matvec(A, dX), dY)]
for i in range(N):
    ok &= check_line(f"∆x{i + 1}", dX[i], r[i])
print("6) Полная трудоёмкость T = t + T·A  (формула (12)):")
r = [a + b for a, b in zip(t, vecmat(T, A))]
for j in range(N):
    ok &= check_line(f"T{j + 1}", T[j], r[j])
print("7) Полная фондоёмкость F = f + F·A:")
r = [a + b for a, b in zip(f, vecmat(Fc, A))]
for j in range(N):
    ok &= check_line(f"F{j + 1}", Fc[j], r[j])
print("8) Баланс труда: Σ Tj·yj = Σ x_j^t (весь живой труд «уходит» в конечный продукт):")
ok &= check_line("Σ Tj·yj", sum(T[j] * Y[j] for j in range(N)), sum(Xt))
print("9) Полные затраты через ряд: C ≈ A + A^2 + A^3 + ... (200 членов):")
S, Pk = [[0.0] * N for _ in range(N)], eye(N)
for _ in range(200):
    Pk = matmul(Pk, A)
    S = [[S[i][j] + Pk[i][j] for j in range(N)] for i in range(N)]
mx = max(abs(S[i][j] - C[i][j]) for i in range(N) for j in range(N))
print(f"   максимальное отличие от C=(E-A)^-1-E: {mx:.1e} -> {'верно' if mx < 1e-6 else 'ОШИБКА'}")
ok &= mx < 1e-6
print()
print("ИТОГ ПРОВЕРКИ:", "все равенства выполняются." if ok else "есть ошибки!")
