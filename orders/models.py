from django.db import models
from shop.models import Product
from accounts.models import User

from cart.models import Kargo

ILLER = [['1', 'Adana'], ['2', 'Adıyaman'], ['3', 'Afyonkarahisar'], ['4', 'Ağrı'], ['5', 'Aksaray'], ['6', 'Amasya'], ['7', 'Ankara'], ['8', 'Antalya'], ['9', 'Ardahan'], ['10', 'Artvin'], ['11', 'Aydın'], ['12', 'Balıkesir'], ['13', 'Bartın'], ['14', 'Batman'], ['15', 'Bayburt'], ['16', 'Bilecik'], ['17', 'Bingöl'], ['18', 'Bitlis'], ['19', 'Bolu'], ['20', 'Burdur'], ['21', 'Bursa'], ['22', 'Çanakkale'], ['23', 'Çankırı'], ['24', 'Çorum'], ['25', 'Denizli'], ['26', 'Diyarbakır'], ['27', 'Düzce'], ['28', 'Edirne'], ['29', 'Elazığ'], ['30', 'Erzincan'], ['31', 'Erzurum'], ['32', 'Eskişehir'], ['33', 'Gaziantep'], ['34', 'Giresun'], ['35', 'Gümüşhane'], ['36', 'Hakkâri'], ['37', 'Hatay'], ['38', 'Iğdır'], ['39', 'Isparta'], ['40', 'İstanbul'], ['41', 'İzmir'], ['42', 'Kahramanmaraş'], ['43', 'Karabük'], ['44', 'Karaman'], ['45', 'Kars'], ['46', 'Kastamonu'], ['47', 'Kayseri'], ['48', 'Kilis'], ['49', 'Kırıkkale'], ['50', 'Kırklareli'], ['51', 'Kırşehir'], ['52', 'Kocaeli'], ['53', 'Konya'], ['54', 'Kütahya'], ['55', 'Malatya'], ['56', 'Manisa'], ['57', 'Mardin'], ['58', 'Mersin'], ['59', 'Muğla'], ['60', 'Muş'], ['61', 'Nevşehir'], ['62', 'Niğde'], ['63', 'Ordu'], ['64', 'Osmaniye'], ['65', 'Rize'], ['66', 'Sakarya'], ['67', 'Samsun'], ['68', 'Şanlıurfa'], ['69', 'Siirt'], ['70', 'Sinop'], ['71', 'Sivas'], ['72', 'Şırnak'], ['73', 'Tekirdağ'], ['74', 'Tokat'], ['75', 'Trabzon'], ['76', 'Tunceli'], ['77', 'Uşak'], ['78', 'Van'], ['79', 'Yalova'], ['80', 'Yozgat'], ['81', 'Zonguldak']]

KARGO_TIPLERI = (
    ('1', 'Kapıda Nakit Ödeme'),
    ('2', 'Kapıda Tek Çekim Kredi Kartı Ödeme'),
    ('3', 'EFT ile Ödeme'),
)
class Order(models.Model):
    kargo_tipi = (models.CharField('Ödeme Tercihiniz:', max_length=10, choices=KARGO_TIPLERI, help_text = "Blabla"))
    first_name = models.CharField("Adınız:", max_length=60)
    last_name = models.CharField("Soyadınız:",max_length=60)
    email = models.EmailField()
    address = models.TextField("Adres:")
    city = models.CharField('Şehir:', max_length=10, choices=ILLER)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField("Ödenme durumu", default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Sipariş'
        verbose_name_plural = "Siparişler"
		

    def __str__(self):
        return 'Sipariş {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem_set.all())
    
    def get_total_kargo(self):
        toplam_agırlık = sum(item.get_agırlık() for item in self.orderitem_set.all())
        kargo = Kargo.objects.first()
        if  kargo.agırlık1 <= toplam_agırlık < kargo.agırlık2:
            return kargo.fiyat1
        if  kargo.agırlık2 <= toplam_agırlık < kargo.agırlık3:
            return kargo.fiyat2
        if  kargo.agırlık3 <= toplam_agırlık < kargo.agırlık4:
            return kargo.fiyat3
        if  kargo.agırlık4 <= toplam_agırlık < kargo.agırlık5:
            return kargo.fiyat4
        if  kargo.agırlık5 <= toplam_agırlık < kargo.agırlık6:
            return kargo.fiyat5
        if  kargo.agırlık6 <= toplam_agırlık < kargo.agırlık7:
            return kargo.fiyat6
        if  kargo.agırlık7 <= toplam_agırlık < kargo.agırlık8:
            return kargo.fiyat7
        if  kargo.agırlık8 <= toplam_agırlık < kargo.agırlık9:
            return kargo.fiyat8
        if  kargo.agırlık9 <= toplam_agırlık < kargo.agırlık10:
            return kargo.fiyat9
        if  kargo.agırlık10 <= toplam_agırlık < kargo.agırlık11:
            return kargo.fiyat10
        if  kargo.agırlık11 <= toplam_agırlık < kargo.agırlık12:
            return kargo.fiyat11
        if  kargo.agırlık12 <= toplam_agırlık < kargo.agırlık13:
            return kargo.fiyat12
        if  kargo.agırlık13 <= toplam_agırlık < kargo.agırlık14:
            return kargo.fiyat13
        if  kargo.agırlık14 <= toplam_agırlık :
            return kargo.fiyat14
	
    def get_total_bedel(self):
        return self.get_total_cost() + self.get_total_kargo() + self.banka_bedel()
    
    def banka_bedel(self):
        if self.kargo_tipi == "3":
            return 0
        else:
            kargo = Kargo.objects.first()
            return kargo.bankacılık_bedeli


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name = "Sipariş")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name = "Ürün")
    price = models.DecimalField("Fiyat", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Miktar", default=1)
    agırlık = models.PositiveIntegerField("Ağırlık", default=0)

    def get_cost(self):
        return self.price * self.quantity
    
    def get_agırlık(self):
        return self.agırlık * self.quantity

