var chatWindow = document.getElementById('chat-container');
var dateSeparator = document.getElementById('date-separator');
var currentDates = document.getElementsByClassName('current-date');

let observer = new IntersectionObserver(entries => {
  // Находим первую видимую дату
  const visibleEntry = entries.find(entry => entry.isIntersecting);
  
  if (visibleEntry) {
    dateSeparator.textContent = visibleEntry.target.textContent;
    dateSeparator.classList.remove('hidden');
    console.log('Visible date:', dateSeparator.textContent);
  } else {
    // Если нет видимых дат, скрываем разделитель
    dateSeparator.classList.add('hidden');
    console.log('No visible dates');
  }
}, { 
  root: chatWindow, 
  threshold: 0.1,
  rootMargin: '-10% 0px -90% 0px' // Настраиваем область пересечения
});

// Наблюдаем за всеми элементами с датами
Array.from(currentDates).forEach(el => observer.observe(el));

// Инициализируем при загрузке
setTimeout(() => {
  chatWindow.scrollTop = chatWindow.scrollHeight;
  // Принудительно проверяем видимость после скролла
  setTimeout(() => {
    Array.from(currentDates).forEach(el => {
      const rect = el.getBoundingClientRect();
      const containerRect = chatWindow.getBoundingClientRect();
      if (rect.top >= containerRect.top && rect.top <= containerRect.bottom) {
        dateSeparator.textContent = el.textContent;
        dateSeparator.classList.remove('hidden');
      }
    });
  }, 100);
}, 100);