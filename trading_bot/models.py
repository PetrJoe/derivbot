from django.db import models

class AnalysisResult(models.Model):
    symbol = models.CharField(max_length=20)
    timeframe = models.CharField(max_length=10)
    recommendation = models.CharField(max_length=10)
    patterns = models.CharField(max_length=255)
    price = models.FloatField()
    rsi = models.FloatField()
    macd = models.FloatField()
    macd_signal = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.symbol} {self.timeframe} - {self.recommendation}"
