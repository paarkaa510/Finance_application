// static/js/charts.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Custom script loaded');

    const expensesData = JSON.parse(document.getElementById('expensesData').textContent);
    const goalsData = JSON.parse(document.getElementById('goalsData').textContent);

    const expensesLabels = expensesData.map(expense => expense.category);
    const expensesAmounts = expensesData.map(expense => expense.total);

    const ctxPie = document.getElementById('expensesPieChart').getContext('2d');
    if (window.expensesPieChart && typeof window.expensesPieChart.destroy === 'function') {
        window.expensesPieChart.destroy();
    }
    window.expensesPieChart = new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: expensesLabels,
            datasets: [{
                data: expensesAmounts,
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']
            }]
        }
    });

    const goalsLabels = goalsData.map(goal => goal.name);
    const targetAmounts = goalsData.map(goal => goal.target_amount);
    const currentAmounts = goalsData.map(goal => goal.current_amount);
    
    const ctxBar = document.getElementById('goalsBarChart').getContext('2d');
    if (window.goalsBarChart && typeof window.goalsBarChart.destroy === 'function') {
        window.goalsBarChart.destroy();
    }
    window.goalsBarChart = new Chart(ctxBar, {
        type: 'bar',
        data: {
            labels: goalsLabels,
            datasets: [
                {
                    label: 'Current Amount',
                    data: currentAmounts,
                    backgroundColor: '#36A2EB'
                },
                {
                    label: 'Target Amount',
                    data: targetAmounts,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)'
                }
            ]
        },
        options: {
            scales: {
                x: {
                    stacked: true
                },
                y: {
                    stacked: true,
                    beginAtZero: true
                }
            }
        }
    });
});


