import json

# Словари для перевода технического формата HH в человеческий
EXPERIENCE_MAP = {
    'noExperience': 'Без опыта',
    'between1And3': 'От 1 года до 3 лет',
    'between3And6': 'От 3 до 6 лет',
    'moreThan6': 'Более 6 лет'
}

FORMAT_MAP = {
    'REMOTE': 'Удаленная работа',
    'HYBRID': 'Гибридный формат',
    'ON_SITE': 'Офис'
}

def parse_salary(comp_dict):
    """Вытаскивает зарплату в читаемый вид, учитывая вилку от и до"""
    if not comp_dict or 'noCompensation' in comp_dict:
        return "Не указана"
    
    sal_from = comp_dict.get('from')
    sal_to = comp_dict.get('to')
    currency = comp_dict.get('currencyCode', 'RUR')
    
    # Определяем, до вычета налогов (gross=True) или на руки (gross=False)
    # По умолчанию считаем "на руки", если поле отсутствует
    gross = comp_dict.get('gross', False)
    tax_info = "до вычета налогов" if gross else "на руки"
    
    if sal_from and sal_to:
        return f"От {sal_from} до {sal_to} {currency} ({tax_info})"
    elif sal_from:
        return f"От {sal_from} {currency} ({tax_info})"
    elif sal_to:
        return f"До {sal_to} {currency} ({tax_info})"
    
    return "Не указана"

def prepare_for_rag(input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
        
    cleaned_docs = []
    
    for item in raw_data:
        # В твоем примере текста описания нет, но в полном ответе по вакансии он должен быть.
        # Если описания нет, вставляем заглушку, чтобы документ не терялся.
        description = item.get('vacancy-description', 'Описание не загружено').strip()
            
        # 1. Собираем метаданные
        company_name = item.get('company', {}).get('name', 'Неизвестная компания')
        vacancy_name = item.get('name', 'Без названия')
        exp_raw = item.get('workExperience', 'unknown')
        experience = EXPERIENCE_MAP.get(exp_raw, exp_raw)
        
        # Обработка workFormats (форматы работы)
        formats_raw = item.get('workFormats', [{}])[0].get('workFormatsElement', [])
        work_format = ", ".join([FORMAT_MAP.get(f, f) for f in formats_raw]) if formats_raw else "Не указан"
        
        # Получаем зарплату, используя обновленную функцию
        salary = parse_salary(item.get('compensation'))
        
        # 2. Формируем единый текст документа для эмбеддинга
        page_content = (
            f"Должность: {vacancy_name}\n"
            f"Компания: {company_name}\n"
            f"Зарплата: {salary}\n"
            f"Опыт работы: {experience}\n"
            f"Формат работы: {work_format}\n"
            f"---\n"
            f"Описание вакансии:\n{description}"
        )
        
        # 3. Упаковываем в стандартный формат для RAG
        doc = {
            "page_content": page_content,
            "metadata": {
                "vacancy_id": item.get('vacancyId'),
                "title": vacancy_name,
                "company": company_name,
                "experience": exp_raw,  
                "has_salary": salary != "Не указана"
            }
        }
        cleaned_docs.append(doc)
        
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(cleaned_docs, f, ensure_ascii=False, indent=2)
        
    print(f"Обработано {len(cleaned_docs)} вакансий. Зарплаты учтены. Данные готовы для RAG.")

# Запуск скрипта
if __name__ == "__main__":
    # Замени на названия своих файлов
    prepare_for_rag('all_datas_updated.json', 'rag_documents.json')