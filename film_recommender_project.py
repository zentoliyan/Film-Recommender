import random

# Film Recommender Project

#region film listesi

# film listelemesi burada yapılıyor

filmler = {
    "aksiyon"   : [
                         "Örümcek-Adam: Örümcek-Evrenine Geçiş", 
                         "Transformers: Canavarların Yükselişi", 
                         "John Wick 4",
                         "Avatar: Suyun Yolu",
                         "Labirent: Ölümcül Kaçış,",
                         "Indiana Jones ve Kader Kadranı",
                         "Hızlı ve Öfkeli 9"
                         ],
    
    "belgesel"   : [
                         "Cartel Land", 
                         "Triumph Of The Will", 
                         "Last Train Home",
                         "Grey Gardens",
                         "To Be And To Have",
                         "Grizzly Man",
                         "Jiro Dreams Of Sushi"
                         ],
    
    "bilimkurgu": [
                         "Inception", 
                         "The Prestige", 
                         "Eternal Sunshine of the Spotless Mind",
                         "Back to the Future",
                         "Interstellar",
                         "The Butterfly Effect",
                         "G.O.R.A."
                         ],
    
    "dramatik"   : [
                         "The Kate Rinner", 
                         "Hugo", 
                         "Lo Impossible",
                         "Titanic",
                         "Seven Pounds",
                         "A Time for Drunken Horses",
                         "Gone Baby Gone"
                         ],

    "gerilim"   : [
                         "Reminiscence", 
                         "1917", 
                         "Malignant",
                         "Joker",
                         "Parasite",
                         "Mortal Kombat",
                         "A Classic Horror Story"
                         ],
    
    "komedi"    : [
                         "The Unbearable Weight of Massive Talent", 
                         "Free Guy", 
                         "The Boss Baby: Family Business",
                         "Yes Day",
                         "The Mitchells vs. the Machines",
                         "The Hitman's Wife's Bodyguard",
                         "The Suicide Squad"
                         ],
    
    "korku"     : [
                         "Black Swan", 
                         "Saw", 
                         "The Others",
                         "Sweeney Todd: The Demon Barber of Fleet Street",
                         "Constantine",
                         "1408",
                         "Resident Evil"
                         ],
    
    "yeşilçam"  : [
                         "Hababam Sınıfı",    
                         "Selvi Boylum Al Yazmalim", 
                         "Süt Kardeşler",
                         "Zügürt Aga",
                         "Aile Şerefi",
                         "Kapıcılar Kralı",
                         "Sakar Şakir"
                         ]
}

#endregion film listesi

# karşılama mesajının ve kategorilerin olduğu kısım
def filmleri_goster():
    print("Merhaba! Film tavsiye programına hoşgeldiniz. \n \nKategoriler:")
    for kategori in filmler:
        print(kategori.capitalize())  # Kategorilerin baş harfini büyük yaparak göster

# film tavsiyesi yapan kısım
# fonksiyonlar burada yer alıyor

def film_oner():
    while True:
        kategori = input("Bir kategori seçin: ").lower()  # kullanıcının girdisini küçük harfe çevir

        if kategori in filmler:
            secilen_filmler = filmler[kategori]
            if len(secilen_filmler) > 0:
                onerilen_film = random.choice(secilen_filmler)
                print(f"Size önerilen film: {onerilen_film}")
            else:
                print("Seçilen kategoriye ait film bulunmamaktadır.")
        else:
            print("Geçersiz bir kategori seçtiniz.")

        devam_et = input("Başka bir film tavsiyesi ister misiniz? (Evet/Hayır): ")
        if devam_et.lower() == "hayır":
            print("Programdan çıkılıyor...")
            return

# programın döngü kısmı
while True:
    filmleri_goster()
    film_oner()
    break

#bitiş
