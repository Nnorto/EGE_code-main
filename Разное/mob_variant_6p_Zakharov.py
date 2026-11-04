# -*- coding: utf-8 -*-
"""
Лабораторная работа «Межотраслевой баланс Леонтьева».
Задача 6, вариант п) из пособия Габидуллиной З.Р. «Математические модели логистики».
Выполнил: Захаров Артём Игоревич, группа 09-301.

Ход решения и форма вывода повторяют пример из пособия (Задача 1а, с. 13–18,
и Задача 2а, с. 18–23): печатаются все промежуточные расчёты, затем проверка.

Числа выводятся с 6 знаками после запятой (как в пособии), хвостовые нули
отбрасываются. Внутри программа считает без округлений.

Запуск:  python mob_variant_6p_Zakharov.py
Нужен только стандартный Python 3 (без сторонних библиотек).
Чтобы решить другой вариант, достаточно поменять исходные данные ниже.
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
# Исходные данные: Задача 6, вариант п) (с. 33 пособия)
# ----------------------------------------------------------------------------
A = [[0.4, 0.1, 0.1],
     [0.3, 0.3, 0.4],
     [0.1, 0.1, 0.2]]          # коэффициенты прямых материальных затрат
Y = [90, 25, 100]              # конечный продукт, млрд руб.
t = [9, 5, 2]                  # прямая трудоёмкость, чел./млн руб.
f = [1, 4, 3]                  # коэффициенты прямых затрат ОПФ (прямая фондоёмкость)
dY_percent = [20, 10, -20]     # ∆y1 = 20%, ∆y2 = 10%, ∆y3 = -20%

print("=" * 78)
print("Лабораторная работа «Межотраслевой баланс Леонтьева»")
print("Задача 6, вариант п)  (Габидуллина З.Р. «Математические модели логистики», с. 27, 33)")
print("Выполнил: Захаров Артём Игоревич, группа 09-301")
print("=" * 78)
print("Решение:")
print()
print("В этой задаче заданы:")
print("1) Матрица коэффициентов прямых материальных затрат i-той про-")
print("дукции на единицу j-той продукции: A=(aij)3x3")
show("   A =", A)
print("2) Вектор конечного продукта")
show("   Y =", column(Y))
print("3) Коэффициенты прямой трудоемкости (чел./млн. руб. = тыс. чел./млрд. руб.)")
print(f"   t = ({', '.join(fm(v) for v in t)})")
print("4) Коэффициенты прямых затрат ОПФ (прямой фондоемкости)")
print(f"   f = ({', '.join(fm(v) for v in f)})")
print("5) Изменения конечного продукта: " +
      "; ".join(f"∆у{i + 1} = {fm(dY_percent[i])}%" for i in range(N)))

# ---------------------------------------------------------------------------
# (E-A), алгебраические дополнения, определитель, обратная матрица
# ---------------------------------------------------------------------------
print()
print("Объем валового продукта по отраслям вычисляется по формуле (3):")
print("X=(E-A)^-1·Y. Для этого нам необходимо знать матрицу (Е-А)^-1.")
E = eye(N)
M = sub(E, A)
print("Вычислим сначала")
show("   E − A =", E, "−", A, "=", M, ".")
print("  Вычислим алгебраические дополнения к элементам матрицы Е-А:")
print()
D = [[0.0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        r = [k for k in range(N) if k != i]
        c = [k for k in range(N) if k != j]
        p, q, s, u = M[r[0]][c[0]], M[r[0]][c[1]], M[r[1]][c[0]], M[r[1]][c[1]]
        D[i][j] = (-1) ** (i + j) * (p * u - q * s)
        end = "." if (i, j) == (N - 1, N - 1) else ","
        print(f"D{i + 1}{j + 1}=(-1)^{i + j + 2}·({fp(p)}·{fp(u)} - {fp(q)}·{fp(s)}) = {fm(D[i][j])}{end}")
m = M
det = (m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[1][0] * m[2][1] * m[0][2]
       - m[0][2] * m[1][1] * m[2][0] - m[0][1] * m[1][0] * m[2][2] - m[1][2] * m[2][1] * m[0][0])
print()
print("Найдем определитель матрицы (Е-А):")
print(f"det(E-A) = {fp(m[0][0])}·{fp(m[1][1])}·{fp(m[2][2])} + {fp(m[0][1])}·{fp(m[1][2])}·{fp(m[2][0])} + "
      f"{fp(m[1][0])}·{fp(m[2][1])}·{fp(m[0][2])} -")
print(f"- {fp(m[0][2])}·{fp(m[1][1])}·{fp(m[2][0])} - {fp(m[0][1])}·{fp(m[1][0])}·{fp(m[2][2])} - "
      f"{fp(m[1][2])}·{fp(m[2][1])}·{fp(m[0][0])} = {fm(det)}.")
if abs(det) < EPS:
    sys.exit("det(E-A) = 0 — обратной матрицы не существует")
print("Тогда по формуле (12) обратная матрица равна:")
B = [[D[j][i] / det for j in range(N)] for i in range(N)]
show("   (E-A)^-1 =", f"1/{fm(det)} ·", D, "^T =")
show("   =", f"1/{fm(det)} ·", transpose(D), "=", B, ".")

# ---------------------------------------------------------------------------
# 1) Изменение валового выпуска и межотраслевых потоков
# ---------------------------------------------------------------------------
print()
print("-" * 78)
print("1) Изменение валового выпуска (∆x) и межотраслевых потоков (∆xij)")
print("-" * 78)
print("Найдем изменения валового продукта для предложенных изменений конечного продукта")
print("; ".join(f"∆у{i + 1} = {fm(dY_percent[i])}%" for i in range(N)) +
      ", для этого определим стоимостное выражение для заданного процентного изменения")
print("конечного продукта:")
dY = [Y[i] * dY_percent[i] / 100 for i in range(N)]
for i in range(N):
    print()
    print(f"{fm(Y[i])} - 100%")
    print(f"∆у{i + 1} - {fm(dY_percent[i])}%")
    print(f"              ∆у{i + 1} = {fm(Y[i])}·{fp(dY_percent[i])}/100 = {fm(dY[i])} млрд. руб.")
show("   ∆Y =", column(dY))
print("Для определения изменений валового продукта воспользуемся формулой (6)")
dX = matvec(B, dY)
show("   ∆X=(E-A)^-1·∆Y =", B, "·", column(dY), "=", column(dX), ".")
for i in range(N):
    terms = " + ".join(f"{fm(B[i][k])}·{fp(dY[k])}" for k in range(N))
    print(f"   ∆x{i + 1} = {terms} = {fm(dX[i])} млрд. руб.")
print("Для расчета изменений межотраслевых потоков применим формулу")
print("∆xij = aij ·∆xj ,")
dx = [[A[i][j] * dX[j] for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        end = "." if (i, j) == (N - 1, N - 1) else ","
        print(f"∆x{i + 1}{j + 1}= a{i + 1}{j + 1}·∆x{j + 1} = {fm(A[i][j])}·{fp(dX[j])} = {fm(dx[i][j])}{end}")
show("   (∆xij)3x3 =", dx, ".")

# ---------------------------------------------------------------------------
# 2) Изменение потребности в трудовых ресурсах
# ---------------------------------------------------------------------------
print()
print("-" * 78)
print("2) Изменение потребности в трудовых ресурсах по отраслям")
print("-" * 78)
print("∆xj^t = tj·∆xj ;  t в чел./млн. руб., ∆x в млрд. руб. (1 млрд = 1000 млн), поэтому")
print("∆xj^t = tj·∆xj·1000 чел. = tj·∆xj тыс. чел.")
dL = [t[j] * dX[j] for j in range(N)]           # тыс. чел.
for j in range(N):
    print(f"   ∆x{j + 1}^t = t{j + 1}·∆x{j + 1} = {fm(t[j])} чел./млн. руб. · {fp(dX[j])} млрд. руб. = "
          f"{fm(t[j])}·{fp(dX[j])}·1000 = {fm(dL[j] * 1000, 2)} чел. ({fm(dL[j])} тыс. чел.)")
print(f"   Всего: ∆L = {fm(sum(dL) * 1000, 2)} чел.")

# ---------------------------------------------------------------------------
# 3) Изменение потребности в ОПФ
# ---------------------------------------------------------------------------
print()
print("-" * 78)
print("3) Изменение потребности в основных производственных фондах по отраслям")
print("-" * 78)
print("∆Фj = fj·∆xj")
dF = [f[j] * dX[j] for j in range(N)]
for j in range(N):
    print(f"   ∆Ф{j + 1} = f{j + 1}·∆x{j + 1} = {fm(f[j])}·{fp(dX[j])} млрд. руб. = {fm(dF[j])} млрд. руб.")
print(f"   Всего: ∆Ф = {fm(sum(dF))} млрд. руб.")

# ---------------------------------------------------------------------------
# 4) Валовой и промежуточный продукт, мат. затраты, условно-чистый продукт
# ---------------------------------------------------------------------------
print()
print("-" * 78)
print("4) Промежуточный и валовый продукт, условно-чистый продукт, материальные затраты")
print("-" * 78)
print("Вычислим объем валового продукта по отраслям по формуле (3)")
X = matvec(B, Y)
show("   X=(E-A)^-1·Y =", B, "·", column(Y), "=", column(X), ".")
for i in range(N):
    terms = " + ".join(f"{fm(B[i][k])}·{fm(Y[k])}" for k in range(N))
    print(f"   x{i + 1} = {terms} = {fm(X[i])} млрд. руб.")
print("Межотраслевые потоки рассчитываются по формуле (8), т.е.")
print(" Xij = aij ·xj ,")
x = [[A[i][j] * X[j] for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        end = "." if (i, j) == (N - 1, N - 1) else ","
        print(f"x{i + 1}{j + 1}= a{i + 1}{j + 1}·x{j + 1} = {fm(A[i][j])}·{fm(X[j])} = {fm(x[i][j])}{end}")
show("   (xij)3x3 =", x, ".")
print("Найдем промежуточный продукт каждой отрасли по формуле")
print("   Σ(j=1..n) xij = xi1 + xi2 + ... + xin .")
inter = [sum(x[i]) for i in range(N)]
for i in range(N):
    print(f"Промежуточный продукт {i + 1}-ой отрасли")
    print(f"   Σ(j=1..n) x{i + 1}j = {' + '.join(fm(v) for v in x[i])} = {fm(inter[i])}.")
print("Материальные затраты в каждую отрасль рассчитываем по формуле")
print("   Σ(i=1..n) xij = x1j + x2j + ... + xnj .")
mat = [sum(x[i][j] for i in range(N)) for j in range(N)]
names = ["первую", "вторую", "третью"]
preps = ["в", "во", "в"]
for j in range(N):
    print(f"Материальные затраты {preps[j]} {names[j]} отрасль")
    print(f"   Σ(i=1..n) xi{j + 1} = {' + '.join(fm(x[i][j]) for i in range(N))} = {fm(mat[j])}.")
print("Вычислим величину условно-чистого продукта (чистого продукта и амортизационных")
print("отчислений) для каждой отрасли по формуле:")
print("   zj = xj − Σ(i=1..n) xij ,")
z = [X[j] - mat[j] for j in range(N)]
for j in range(N):
    end = "." if j == N - 1 else ","
    print(f"   z{j + 1} = {fm(X[j])} − {fm(mat[j])} = {fm(z[j])}{end}")

# ---------------------------------------------------------------------------
# 5) Косвенные затраты 1-го порядка и полные затраты
# ---------------------------------------------------------------------------
print()
print("-" * 78)
print("5) Матрицы коэффициентов косвенных материальных затрат 1-го порядка и полных затрат")
print("-" * 78)
print("Коэффициенты косвенных материальных затрат 1-го порядка:")
print("   aij^(1) = ai1·a1j + ai2·a2j + ... + ain·anj ,")
A2 = matmul(A, A)
for i in range(N):
    for j in range(N):
        terms = " + ".join(f"{fm(A[i][k])}·{fm(A[k][j])}" for k in range(N))
        print(f"   a{i + 1}{j + 1}^(1) = {terms} = {fm(A2[i][j])}")
show("   A^(1) = A^2 = A×A =", A2, ".")
print("Матрица коэффициентов полных материальных затрат (формула (10)):")
print("                         С=(Е-А)^-1 - Е.")
C = sub(B, E)
show("   C=(E-A)^-1 − E =", B, "−", E, "=", C, ".")

# ---------------------------------------------------------------------------
# 6) Совокупные затраты живого труда
# ---------------------------------------------------------------------------
print()
print("-" * 78)
print("6) Совокупные затраты живого труда в каждой отрасли")
print("-" * 78)
L = [t[j] * X[j] for j in range(N)]              # тыс. чел.
print("Затраты живого труда при исходном выпуске: xj^t = tj·xj")
for j in range(N):
    print(f"   x{j + 1}^t = {fm(t[j])}·{fm(X[j])} = {fm(L[j])} тыс. чел. = {fm(L[j] * 1000, 2)} чел.")
print("Совокупная потребность в трудовых ресурсах по отраслям с учетом изменений")
print("конечного продукта:  xj^t + ∆xj^t = tj·(xj + ∆xj).")
print("Сначала вычислим xj + ∆xj :")
X1 = [X[j] + dX[j] for j in range(N)]
for j in range(N):
    end = "." if j == N - 1 else ","
    print(f"   x{j + 1}+∆x{j + 1} = {fm(X[j])} + {fp(dX[j])} = {fm(X1[j])}{end}")
L1 = [t[j] * X1[j] for j in range(N)]
print("Тогда совокупная потребность в трудовых ресурсах по отраслям:")
for j in range(N):
    print(f"   x{j + 1}^t+∆x{j + 1}^t = {fm(t[j])}·{fm(X1[j])} = {fm(L1[j])} тыс. чел. = {fm(L1[j] * 1000, 2)} чел.")
print("Коэффициенты полной трудоемкости (формула (13)):")
T = vecmat(t, B)
show("   T = t·(E-A)^-1 =", [t], "·", B, "=")
print(f"   = ({', '.join(fm(v) for v in T)}) чел./млн. руб.")
for j in range(N):
    terms = " + ".join(f"{fm(t[k])}·{fm(B[k][j])}" for k in range(N))
    print(f"   T{j + 1} = {terms} = {fm(T[j])}")
LT = [T[j] * Y[j] for j in range(N)]
print("Полные затраты труда, воплощенные в конечном продукте отрасли: Tj·yj")
for j in range(N):
    print(f"   T{j + 1}·y{j + 1} = {fm(T[j])}·{fm(Y[j])} = {fm(LT[j])} тыс. чел.")

# ---------------------------------------------------------------------------
# 7) Совокупные затраты ОПФ
# ---------------------------------------------------------------------------
print()
print("-" * 78)
print("7) Совокупные затраты ОПФ в каждой отрасли")
print("-" * 78)
Ph = [f[j] * X[j] for j in range(N)]
print("Потребность в ОПФ при исходном выпуске: Фj = fj·xj")
for j in range(N):
    print(f"   Ф{j + 1} = {fm(f[j])}·{fm(X[j])} = {fm(Ph[j])} млрд. руб.")
print("Совокупная потребность в ОПФ с учетом изменения конечного продукта:")
print("   Фj + ∆Фj = fj·(xj + ∆xj)")
Ph1 = [f[j] * X1[j] for j in range(N)]
for j in range(N):
    print(f"   Ф{j + 1}+∆Ф{j + 1} = {fm(f[j])}·{fm(X1[j])} = {fm(Ph1[j])} млрд. руб.")
print("Коэффициенты полной фондоемкости (формула (18)):")
Fc = vecmat(f, B)
show("   F = f·(E-A)^-1 =", [f], "·", B, "=")
print(f"   = ({', '.join(fm(v) for v in Fc)}).")
for j in range(N):
    terms = " + ".join(f"{fm(f[k])}·{fm(B[k][j])}" for k in range(N))
    print(f"   F{j + 1} = {terms} = {fm(Fc[j])}")
FY = [Fc[j] * Y[j] for j in range(N)]
print("Полные затраты ОПФ, воплощенные в конечном продукте отрасли: Fj·yj")
for j in range(N):
    print(f"   F{j + 1}·y{j + 1} = {fm(Fc[j])}·{fm(Y[j])} = {fm(FY[j])} млрд. руб.")

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
ok &= check_line("det(E-A)", sum(M[0][j] * D[0][j] for j in range(N)), det)
print("3) В правильности расчетов можно убедиться, проверив выполнение равенства X=A·X+Y:")
r = [a + y for a, y in zip(matvec(A, X), Y)]
for i in range(N):
    ok &= check_line(f"x{i + 1}", X[i], r[i])
print("4) ∆X = A·∆X + ∆Y:")
r = [a + y for a, y in zip(matvec(A, dX), dY)]
for i in range(N):
    ok &= check_line(f"∆x{i + 1}", dX[i], r[i])
print("5) Строки баланса: промежуточный продукт + конечный продукт = валовой продукт")
for i in range(N):
    ok &= check_line(f"Σx{i + 1}j + y{i + 1}", inter[i] + Y[i], X[i])
print("6) Столбцы баланса: материальные затраты + условно-чистый продукт = валовой продукт")
for j in range(N):
    ok &= check_line(f"Σxi{j + 1} + z{j + 1}", mat[j] + z[j], X[j])
print("7) Σ zj = Σ yj (условно-чистый продукт равен конечному продукту в целом)")
ok &= check_line("Σz = Σy", sum(z), sum(Y))
print("8) Полная трудоёмкость T = t + T·A  и баланс труда Σ Tj·yj = Σ tj·xj")
r = [a + b for a, b in zip(t, vecmat(T, A))]
for j in range(N):
    ok &= check_line(f"T{j + 1}", T[j], r[j])
ok &= check_line("Σ Tj·yj = Σ tj·xj", sum(LT), sum(L))
print("9) Полная фондоёмкость F = f + F·A  и баланс ОПФ Σ Fj·yj = Σ fj·xj")
r = [a + b for a, b in zip(f, vecmat(Fc, A))]
for j in range(N):
    ok &= check_line(f"F{j + 1}", Fc[j], r[j])
ok &= check_line("Σ Fj·yj = Σ fj·xj", sum(FY), sum(Ph))
print("10) Полные затраты через ряд: C ≈ A + A^2 + A^3 + ... (200 членов)")
S, Pk = [[0.0] * N for _ in range(N)], eye(N)
for _ in range(200):
    Pk = matmul(Pk, A)
    S = [[S[i][j] + Pk[i][j] for j in range(N)] for i in range(N)]
mx = max(abs(S[i][j] - C[i][j]) for i in range(N) for j in range(N))
print(f"   максимальное отличие от C=(E-A)^-1-E: {mx:.1e} -> {'верно' if mx < 1e-6 else 'ОШИБКА'}")
ok &= mx < 1e-6
print("11) Новый валовой выпуск: X+∆X = (E-A)^-1·(Y+∆Y)")
r = matvec(B, [Y[i] + dY[i] for i in range(N)])
for i in range(N):
    ok &= check_line(f"x{i + 1}+∆x{i + 1}", X1[i], r[i])
print()
print("ИТОГ ПРОВЕРКИ:", "все равенства выполняются." if ok else "есть ошибки!")

# ----------------------------------------------------------------------------
# Сводная таблица
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("СВОДНАЯ ТАБЛИЦА (млрд руб.; труд — чел.)")
print("=" * 78)
hdr = ["Отрасль", "x_j", "∆x_j", "x_j+∆x_j", "Мат.затр.", "z_j", "∆L_j, чел.", "∆Ф_j"]
print("".join(h.rjust(13) for h in hdr))
for j in range(N):
    row = [str(j + 1), fm(X[j], 4), fm(dX[j], 4), fm(X1[j], 4), fm(mat[j], 4), fm(z[j], 4),
           fm(dL[j] * 1000, 2), fm(dF[j], 4)]
    print("".join(v.rjust(13) for v in row))
