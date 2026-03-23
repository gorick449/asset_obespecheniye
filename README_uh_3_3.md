# Каталог `uh_3_3`

Каталог **uh_3_3** содержит материалы оценки и проработки функциональных требований по контуру снабжения и обеспечения в проекте на базе **1С:Управление холдингом** (имя каталога отражает ветку/версию контекста оценки — **3.3**).

Здесь собраны текстовые отчёты по требованиям с номерами **10–64**: ведение НСИ, аналоги, заявки и планы потребности, план и программа закупок, лоты и тендеры, ценообразование, заказы поставщикам, склад и перемещения, СИЗ, учёт прослеживаемости (РНПТ), отчёты и интеграции с внешними системами. Для части требований (строки **14–23**) рядом с основным отчётом лежат файлы **`*_constrains.md`** с допущениями и ограничениями по пункту; по интеграциям **62–64** могут быть дополнительные файлы **`*_asset.md`**.

**Единица оценки:** все трудозатраты в сводных таблицах и отчётах указаны в **человеко-днях** (чел.-дни) — это оценка объёма работ одного специалиста за один рабочий день. В [total_asset.md](uh_3_3/total_asset.md) для блока «Разработка» приведены варианты **min** / **likely** / **max** (пессимистичный, наиболее вероятный и оптимистичный сценарий).

---

## Расшифровка сокращений

| Сокращение | Расшифровка |
|------------|-------------|
| **УХ** | **1С:Управление холдингом** (конфигурация, в контексте данного каталога) |
| **ERP** | система класса ERP; в смежных отчётах — **1С:ERP Управление предприятием** |
| **УП** | подсистема/конфигурация «Управление предприятием» |
| **НСИ** | нормативно-справочная информация |
| **ФТ** | функциональные требования |
| **ТРУ** | товары, работы, услуги |
| **ПЗ** | план закупок |
| **ИСУ** | информационная система управления (в т.ч. ИСУ Тендер, ИСУ Снабжение / СИП — по контексту отчётов) |
| **КИС** | корпоративная информационная система |
| **КССС** | контур централизованных справочников / кодов НСИ (интеграция с КИС КССС) |
| **КЭД.БД** | компонент КИС «КЭД», база договоров |
| **СИЗ** | средства индивидуальной защиты |
| **РНПТ** | регистрационный номер партии товара (прослеживаемость) |
| **ТН ВЭД** | товарная номенклатура внешнеэкономической деятельности |
| **ФНС** | Федеральная налоговая служба |
| **ЭДО** | электронный документооборот |
| **ЗКП** | запрос коммерческих предложений |
| **КП** | коммерческое предложение |
| **BSL** | встроенный язык 1С (анализ кода конфигурации) |
| **СКД** | система компоновки данных (отчёты) |
| **РС** | регистр сведений |
| **БП** | бизнес-процесс |
| **MXL** | макет (в т.ч. печатная форма 1С) |
| **M:N** | связь «многие ко многим» |
| **ID** | идентификатор (в т.ч. идентификатор потребности) |
| **min / likely / max** | нижняя, наиболее вероятная и верхняя оценка в чел.-днях |
| **ГМ, ГЭ, ГТ** | службы заказчика (главный механик, главный энергетик, главный технолог и др. — по маршрутам согласования) |
| **ИТ, АХО** | информационные технологии; административно-хозяйственный отдел |
| **ДХНО** | длительно неиспользуемые остатки (контекст отчётов по запасам) |
| **ЕПУ** | единое планирование и обеспечение (контекст назначений и потребности) |
| **MVP** | минимально жизнеспособная версия (минимальный объём для первого релиза) |
| **лтх** | префикс объектов/отчётов доработок в конфигурации (по текстам отчётов) |

---

## Файлы в `uh_3_3`

В начале списка — сводные документы:

| Файл | Назначение |
|------|------------|
| [total_asset.md](uh_3_3/total_asset.md) | Сводный файл оценки разработки (таблица по требованиям, min/likely/max в чел.-днях, ссылки на детальные отчёты). |
| [summarize.md](uh_3_3/summarize.md) | Сводный файл по допущениям, ограничениям, рискам и вариантам реализации (по группам ФТ). |

Детальные отчёты и сопутствующие материалы по пунктам требований:

| Файл | Тема (кратко) |
|------|----------------|
| [10_kategorizatsiya_nomenklatury.md](uh_3_3/10_kategorizatsiya_nomenklatury.md) | Категоризация номенклатуры |
| [11_normativy_zapasov.md](uh_3_3/11_normativy_zapasov.md) | Нормативы запасов |
| [12_vedenie_analogov.md](uh_3_3/12_vedenie_analogov.md) | Ведение аналогов номенклатуры |
| [13_avtopodbor_analogov.md](uh_3_3/13_avtopodbor_analogov.md) | Автоподбор аналогов |
| [14_zayavochnye_kampanii.md](uh_3_3/14_zayavochnye_kampanii.md) | Заявочные кампании |
| [14_constrains.md](uh_3_3/14_constrains.md) | Допущения и ограничения (строка 14) |
| [15_zayavka_na_potrebnost_i_obespechenie.md](uh_3_3/15_zayavka_na_potrebnost_i_obespechenie.md) | Заявка на потребность и обеспечение |
| [15_constrains.md](uh_3_3/15_constrains.md) | Допущения и ограничения (строка 15) |
| [16_korrektirovka_potrebnosti.md](uh_3_3/16_korrektirovka_potrebnosti.md) | Корректировка потребности |
| [16_constrains.md](uh_3_3/16_constrains.md) | Допущения и ограничения (строка 16) |
| [17_soglasovanie_zayavki_na_potrebnost.md](uh_3_3/17_soglasovanie_zayavki_na_potrebnost.md) | Согласование заявки на потребность |
| [17_constrains.md](uh_3_3/17_constrains.md) | Допущения и ограничения (строка 17) |
| [18_obrabotka_potrebnostey_i_sposob_obespecheniya.md](uh_3_3/18_obrabotka_potrebnostey_i_sposob_obespecheniya.md) | Обработка потребностей и способ обеспечения |
| [18_constrains.md](uh_3_3/18_constrains.md) | Допущения и ограничения (строка 18) |
| [19_sposoby_obespecheniya.md](uh_3_3/19_sposoby_obespecheniya.md) | Способы обеспечения |
| [19_constrains.md](uh_3_3/19_constrains.md) | Допущения и ограничения (строка 19) |
| [20_formirovanie_plana_potrebnosti.md](uh_3_3/20_formirovanie_plana_potrebnosti.md) | Формирование плана потребности |
| [20_constrains.md](uh_3_3/20_constrains.md) | Допущения и ограничения (строка 20) |
| [21_soglasovanie_plana_potrebnosti.md](uh_3_3/21_soglasovanie_plana_potrebnosti.md) | Согласование плана потребности |
| [21_constrains.md](uh_3_3/21_constrains.md) | Допущения и ограничения (строка 21) |
| [22_zayavki_na_zakupku_i_stroki_plana_zakupok.md](uh_3_3/22_zayavki_na_zakupku_i_stroki_plana_zakupok.md) | Заявки на закупку и строки плана закупок |
| [22_constrains.md](uh_3_3/22_constrains.md) | Допущения и ограничения (строка 22) |
| [23_soglasovanie_zayavok_na_zakupku.md](uh_3_3/23_soglasovanie_zayavok_na_zakupku.md) | Согласование заявок на закупку |
| [23_constrains.md](uh_3_3/23_constrains.md) | Допущения и ограничения (строка 23) |
| [24_formirovanie_plana_programmy_zakupok.md](uh_3_3/24_formirovanie_plana_programmy_zakupok.md) | План / программа закупок |
| [25_id_potrebnosti_konsolidatsiya.md](uh_3_3/25_id_potrebnosti_konsolidatsiya.md) | ID потребности при консолидации |
| [26_soglasovanie_plana_programmy_zakupok.md](uh_3_3/26_soglasovanie_plana_programmy_zakupok.md) | Согласование плана / программы закупок |
| [27_korrektirovochnye_plany_zakupok.md](uh_3_3/27_korrektirovochnye_plany_zakupok.md) | Корректировочные планы закупок |
| [28_formirovanie_lotov.md](uh_3_3/28_formirovanie_lotov.md) | Формирование лотов |
| [29_planirovanie_tenderov.md](uh_3_3/29_planirovanie_tenderov.md) | Планирование тендеров |
| [30_vvod_dannykh_o_pobeditele_tendera.md](uh_3_3/30_vvod_dannykh_o_pobeditele_tendera.md) | Данные о победителе тендера |
| [31_tendernaya_dokumentatsiya_po_shablonam.md](uh_3_3/31_tendernaya_dokumentatsiya_po_shablonam.md) | Тендерная документация по шаблонам |
| [32_sbor_i_analiz_predlozheniy_postavshchikov.md](uh_3_3/32_sbor_i_analiz_predlozheniy_postavshchikov.md) | Сбор и анализ предложений поставщиков |
| [33_zagruzka_cen_pobeditelya.md](uh_3_3/33_zagruzka_cen_pobeditelya.md) | Загрузка цен победителя |
| [34_zagruzka_cen_iz_vneshnih_istochnikov.md](uh_3_3/34_zagruzka_cen_iz_vneshnih_istochnikov.md) | Загрузка цен из внешних источников |
| [35_raschet_ceny_posledney_zakupki.md](uh_3_3/35_raschet_ceny_posledney_zakupki.md) | Цена последней закупки |
| [36_soglasovanie_indikativnyh_planovyh_cen_zakupki.md](uh_3_3/36_soglasovanie_indikativnyh_planovyh_cen_zakupki.md) | Индикативные плановые цены закупки |
| [37_generatsiya_zakazov_postavshiku.md](uh_3_3/37_generatsiya_zakazov_postavshiku.md) | Генерация заказов поставщику |
| [38_postuplenie_na_sklad.md](uh_3_3/38_postuplenie_na_sklad.md) | Поступление на склад |
| [39_zayavki_na_peremeschenie.md](uh_3_3/39_zayavki_na_peremeschenie.md) | Заявки на перемещение |
| [40_izmenenie_naznacheniya_potrebnosti.md](uh_3_3/40_izmenenie_naznacheniya_potrebnosti.md) | Изменение назначения потребности |
| [41_rassylki_uvedomleniya.md](uh_3_3/41_rassylki_uvedomleniya.md) | Рассылки и уведомления |
| [42_normativy_vydachi_siz.md](uh_3_3/42_normativy_vydachi_siz.md) | Нормативы выдачи СИЗ |
| [43_plan_potrebnosti_siz.md](uh_3_3/43_plan_potrebnosti_siz.md) | План потребности в СИЗ |
| [44_uchet_vydachi_siz.md](uh_3_3/44_uchet_vydachi_siz.md) | Учёт выдачи СИЗ |
| [45_kontrol_peremescheniy_siz.md](uh_3_3/45_kontrol_peremescheniy_siz.md) | Контроль перемещений СИЗ |
| [46_priznak_proslezhivaemosti_kody_tn_ved.md](uh_3_3/46_priznak_proslezhivaemosti_kody_tn_ved.md) | Прослеживаемость, коды ТН ВЭД |
| [47_avtomaticheskaya_proverka_rnpt_veb_servis_fns.md](uh_3_3/47_avtomaticheskaya_proverka_rnpt_veb_servis_fns.md) | Проверка РНПТ (веб-сервис ФНС) |
| [48_integratsiya_edo_zapolnenie_rnpt.md](uh_3_3/48_integratsiya_edo_zapolnenie_rnpt.md) | ЭДО и заполнение РНПТ |
| [49_kontrol_ostatkov_rnpt_po_partiyam.md](uh_3_3/49_kontrol_ostatkov_rnpt_po_partiyam.md) | Остатки по РНПТ по партиям |
| [50_avtomaticheskie_uvedomleniya_fns_proslezhivaemye.md](uh_3_3/50_avtomaticheskie_uvedomleniya_fns_proslezhivaemye.md) | Уведомления ФНС по прослеживаемым товарам |
| [51_otchety_po_analogam.md](uh_3_3/51_otchety_po_analogam.md) | Отчёты по аналогам |
| [52_sostoyanie_potrebnosti.md](uh_3_3/52_sostoyanie_potrebnosti.md) | Состояние потребности |
| [53_obespechennost_siz.md](uh_3_3/53_obespechennost_siz.md) | Обеспеченность СИЗ |
| [54_sostoyanie_zapasov.md](uh_3_3/54_sostoyanie_zapasov.md) | Состояние запасов |
| [55_plan_fakt_postupleniya.md](uh_3_3/55_plan_fakt_postupleniya.md) | План-факт поступления |
| [56_plan_fakt_zakupok_tenderov_postavok.md](uh_3_3/56_plan_fakt_zakupok_tenderov_postavok.md) | План-факт закупок, тендеров, поставок |
| [57_grafik_postavok.md](uh_3_3/57_grafik_postavok.md) | График поставок |
| [58_sravnitelnyy_analiz_tsen.md](uh_3_3/58_sravnitelnyy_analiz_tsen.md) | Сравнительный анализ цен |
| [59_analiz_tru_365_dney.md](uh_3_3/59_analiz_tru_365_dney.md) | Анализ ТРУ за 365 дней |
| [60_integratsiya_s_erp.md](uh_3_3/60_integratsiya_s_erp.md) | Интеграция с ERP |
| [61_integratsiya_isu_tender.md](uh_3_3/61_integratsiya_isu_tender.md) | Интеграция с ИСУ Тендер |
| [62_integratsiya_isu_snabzhenie.md](uh_3_3/62_integratsiya_isu_snabzhenie.md) | Интеграция с ИСУ Снабжение |
| [62_integratsiya_isu_snabzhenie_asset.md](uh_3_3/62_integratsiya_isu_snabzhenie_asset.md) | Доп. материал по оценке — ИСУ Снабжение |
| [63_integratsiya_kis_ksss.md](uh_3_3/63_integratsiya_kis_ksss.md) | Интеграция с КИС КССС |
| [63_integratsiya_kis_ksss_asset.md](uh_3_3/63_integratsiya_kis_ksss_asset.md) | Доп. материал по оценке — КИС КССС |
| [64_integratsiya_kis_ked_bd.md](uh_3_3/64_integratsiya_kis_ked_bd.md) | Интеграция с КИС КЭД.БД |
| [64_integratsiya_kis_ked_bd_asset.md](uh_3_3/64_integratsiya_kis_ked_bd_asset.md) | Доп. материал по оценке — КИС КЭД.БД |

Подробные оценки и пути к исходным артефактам (в т.ч. `specs/`, `1-asset_report/`) см. в ссылках внутри [total_asset.md](uh_3_3/total_asset.md) и [summarize.md](uh_3_3/summarize.md).
