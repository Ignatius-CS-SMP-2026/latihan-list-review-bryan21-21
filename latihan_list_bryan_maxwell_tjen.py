nu = [75,55,90,85,45,95,80]
print("data nilai asli:", nu)
nu.sort(reverse=True)
print("data setelah ujian diurutkan(descending):",nu)
top_tiga = nu[:3]
print("tiga nilai tertinggi (penerima beasiswa):",top_tiga)
lulus = [n for n in nu if n>=60]
print("daftar nilai yang lulus:",lulus)