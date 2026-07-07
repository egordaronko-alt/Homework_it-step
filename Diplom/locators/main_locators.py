from fontTools.subset.svg import xpath

from Diplom.pages.elements import WebElement, ManyWebElements
from Diplom.pages.base_page import WebPage
import os


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_PAGE") or 'https://belgee.by/'
        super().__init__(web_driver, url)

    def go_to_model_page(self, model_name):
        url = f"https://belgee.by/models/{model_name}"
        self.get(url)
        return self

#accept cookies
    accept_cookie = WebElement(css_selector='.button.big._js-b-cookie-alert._js-cookie-save-all')
#close pop window
    pop_window = WebElement(css_selector='.close._js-pop-close')

#Тестирование хедера Belgee.by
#Локаторы моделей
    models_switcher = WebElement(css_selector='div.w-header-inset-dropper._js-header-inset-dropper')
    header_models = WebElement(css_selector='span.dashed')
    many_models = ManyWebElements(css_selector='.col-md-3.col-sm-3.col-4.pb-10')
#Локаторы ссылок на модели
    model_S50_link = WebElement(css_selector='img[src*="w300_h200_dzylmn18v0ls4xg1bgep.png"]')
    model_X50_link = WebElement(css_selector='img[src*="w300_h200_uogzrfwzjdl9svcpzj57.png"]')
    model_X50plus_link = WebElement(css_selector='img[src*="w300_h200_44a9oqstp6l9jkoe7kui.png"]')
    model_X70_link = WebElement(css_selector='img[src*="w300_h200_m9xovvg3ffjp3bh9xmjl.png"]')
    model_X80_link = WebElement(css_selector="img[src*='w300_h200_f5y8il8onsgrnqplsmeg.png']")

#Тестирование футера "Специальные предложения"
    special_deal_menu = WebElement(xpath='//span[text()="Специальные предложения"]')
    special_deal_promo = WebElement(xpath='//a[@href="https://belgee.by/promo" and text()="Акции"]')
    special_deal_leasing = WebElement(xpath='//a[@href="https://belgee.by/lizing" and text()="Лизинг"]')
    special_deal_kredit = WebElement(xpath='//a[@href="https://belgee.by/kredit" and text()="Кредит"]')

#Тестирование "Владельцу"
    owner_main_link = WebElement(xpath='//li/a/span[text()="Владельцу"]')
    owner_user_manual = WebElement(css_selector='a[href="https://belgee.by/manual"][class="__link"]')
    owner_hundred_belgee = WebElement(css_selector='a[href="https://belgee.by/sto"][class="__link"]')
    owner_core_values = WebElement(css_selector='a[href="https://belgee.by/service-values"][class="__link"]')
    owner_expluatation_advice = WebElement(css_selector='a[href="https://belgee.by/sovety-po-ekspluatacii-avtomobilya-belgee"][class ="__link"]')
    owner_info_line = WebElement(css_selector='a[href="https://belgee.by/infoliniya-belgee"][class="__link"]')
    owner_road_help = WebElement(css_selector='a[href="https://belgee.by/pomosh-na-dorogah-kruglosutochnaya-podderzhka-vladelcev-belgee"][class="__link"]')

#Тестирование "СЗАО БЕЛДЖИ"
    czao_main_link = WebElement(xpath='//li/a/span[text()="СЗАО БЕЛДЖИ"]')
    czao_news = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/news"]')
    czao_about = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/about"]')
    czao_suppliers = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/postavshikam"]')
    czao_diller = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/stat-dilerom"]')
    czao_hotel = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/gostinica"]')
    czao_shop = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/magazin"]')
    czao_corruption = WebElement(css_selector='li div ul li a[href="https://belgee.by/protivodejstvie-korrupcii"]')
    czao_vacancy = WebElement(css_selector='li div ul li a[href="https://belgee.by/vakansii"]')
#Тестирование "Свяжитесь с нами"
    connect_with_us = WebElement(xpath='//span[@class="dashed" and text()="Свяжитесь с нами"]')
#Тестирование "belgee.by"
    belgee_link = WebElement(xpath='//span[@class="dashed" and text()="Автомобили Geely"]')
#Функциональное тестирование стрелок 1/8

    number_of_picture = WebElement(xpath='//div[@class="_js-index-slider-counter slider-counter bold"]')
    main_arrow_left = WebElement(css_selector='div._js-b-index-owl-slider-prev.arrow')
    main_arrow_right = WebElement(css_selector='div._js-b-index-owl-slider-next.arrow')

    image_1 = WebElement(css_selector='img[alt="Главная - слайд 1"][title="Главная - слайд 1"]')
    image_2 = WebElement(css_selector='img[alt="Главная - слайд 2"][title="Главная - слайд 2"]')
    image_3 = WebElement(css_selector='img[alt="Главная - слайд 3"][title="Главная - слайд 3"]')
    image_4 = WebElement(css_selector='img[alt="Главная - слайд 4"][title="Главная - слайд 4"]')
    image_5 = WebElement(css_selector='img[alt="Главная - слайд 5"][title="Главная - слайд 5"]')
    image_6 = WebElement(css_selector='img[alt="Главная - слайд 6"][title="Главная - слайд 6"]')
    image_7 = WebElement(css_selector='img[alt="Главная - слайд 7"][title="Главная - слайд 7"]')
    image_8 = WebElement(css_selector='img[alt="Главная - слайд 8"][title="Главная - слайд 8"]')


#Функциональное тестирование стрелок из 6 картинок
    picture1 = WebElement(css_selector='div.r-box div.r-img[style*="https://belgee.by/storage/thumbs/news/505/w560_h300_uzboexnbuwzixg6uacl4.jpg"]')
    picture2 = WebElement(css_selector='div.r-box div.r-img[style*="https://belgee.by/storage/thumbs/news/502/w560_h300_asfqwwfjyyeoutq5f2vv.png"]')

    picture3 = WebElement(css_selector='div.r-box div.r-img[style*="https://belgee.by/storage/thumbs/news/493/w560_h300_66tlpv8cwefrpfwfnqyz.png"]')
    picture4 = WebElement(css_selector='div.r-box div.r-img[style*="https://belgee.by/storage/thumbs/news/485/w560_h300_oomuqfsan93ghpjsdnpo.png"]')
    picture5 = WebElement(css_selector='div.r-box div.r-img[style*="https://belgee.by/storage/thumbs/news/481/w560_h300_d7n01zltd3gthr0bxoqt.png"]')
    picture6 = WebElement(css_selector='div.r-box div.r-img[style*="https://belgee.by/storage/thumbs/news/470/w560_h300_kfguilo2ngw64ma1mrup.jpg"]')
    arrow = WebElement(css_selector='div._js-b-index-news-slider-next.arrow')

#Перемещение изображений на главной странице сайта
    move_picture1 = WebElement(xpath='/html/body/div/section[3]/div/div[1]/div/div[3]/div/div/a/div/div/div/div[2]/picture/img')
    move_picture2 = WebElement(xpath='/html/body/div[1]/section[3]/div/div[1]/div/div[1]/div/div/a/div/div/div/div[2]/picture/img')
    owl_dots = ManyWebElements(xpath='//div[contains(@class,"owl-dots")]//div')

#Проверка анимаций CSS футера
    #Website creator
    site_developer = WebElement(css_selector='.developer .w-icon-left>.icon')
    developer = WebElement(css_selector='a[href="https://zmitroc.by"]')
    #Social icons
    icon_of_telegram = WebElement(css_selector="a.social-colored-icon__link.tg")
    icon_of_instagram = WebElement(css_selector="a.social-colored-icon__link.ig")
    icon_of_youtube = WebElement(css_selector="a.social-colored-icon__link.yt")
    icon_of_tiktok = WebElement(css_selector="a.social-colored-icon__link.tt")


#S50 page test
    new_s50_button = WebElement(xpath='//a[text()="Новый S50" and @class="tab__link _js-b-ancor"]')
    rows_visible = WebElement(css_selector='._js-image-aside-slider-counter1.slider-counter.bold')
    comfort_button = WebElement(xpath='//a[text()="Комфорт" and @class="tab__link _js-b-ancor"]')
    comfort_banner = WebElement(css_selector='.s-name._h2.bold.align-center.xl-mb-30.mb-20')
    functionality_button = WebElement(xpath='//a[text()="Функциональность" and @class="tab__link _js-b-ancor"]')
    price_list_button = WebElement(xpath='//a[@class="tab__link" and normalize-space(text())="Прайс лист"]')
    bid_button = WebElement(xpath='//a[@class="button orange block _js-b-ancor" and normalize-space(text())="Оставить заявку"]')


#S50 canvas exterier test
    exterier_button = WebElement(xpath='//a[@data-tabs-id="id-tab-level_001" and normalize-space(text())="Экстерьер"]')
    interier_button = WebElement(xpath='//a[@data-tabs-id="id-tab-level_001" and normalize-space(text())="Интерьер"]')
    canvas_exterier = WebElement()


#S50 colors
    all_colors = ManyWebElements(xpath='//a[contains(@data-color-folder, "https://belgee.by/storage/colors/") and contains(@class, "color-switcher__link")]')

#S50 canvas
    canvas_360 = WebElement(css_selector='#car-model-360 canvas')

#Submit_an_application
    submit_image = WebElement(xpath='//img[@alt="Оформить заявку на автомобиль" and @title="Оформить заявку на автомобиль"]')

    dealer_dropdown = WebElement(xpath='//span[contains(@class, "select2-container") and contains(@class, "select2-container--default")]')
    dealer_fields = ManyWebElements(css_selector='li.select2-results__option')

    equipment_dropdown = WebElement(xpath='//select[@name="equipment_id"]/following-sibling::span[contains(@class, "select2")]')
    equipment_fields = ManyWebElements(css_selector='li.select2-results__option')
    # full_name_field =
    # phone_field =
    # email_field =
    # personal_information_field =
