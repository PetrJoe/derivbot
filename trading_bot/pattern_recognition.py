class PatternRecognition:
    def __init__(self, df):
        self.df = df
        self.patterns = {}
        self.analyze_patterns()
        
    def analyze_patterns(self):
        """Analyze various chart patterns"""
        self.check_double_top()
        self.check_double_bottom()
        self.check_head_shoulders()
        # Add more pattern checks as needed
        
    def check_double_top(self):
        """Check for double top pattern"""
        recent = self.df['close'].tail(20).values
        if len(recent) >= 10:
            max1 = recent[:10].max()
            max2 = recent[10:].max()
            if abs(max1 - max2) / max1 < 0.01:
                self.patterns['Double Top'] = {
                    'detected': True,
                    'signal': 'Sell',
                    'confidence': 0.7
                }
                
    def check_double_bottom(self):
        """Check for double bottom pattern"""
        recent = self.df['close'].tail(20).values
        if len(recent) >= 10:
            min1 = recent[:10].min()
            min2 = recent[10:].min()
            if abs(min1 - min2) / min1 < 0.01:
                self.patterns['Double Bottom'] = {
                    'detected': True,
                    'signal': 'Buy',
                    'confidence': 0.7
                }
                
    def check_head_shoulders(self):
        """Simple head and shoulders pattern detection"""
        # Simplified implementation
        recent = self.df['close'].tail(30).values
        if len(recent) >= 30:
            # Check for head and shoulders pattern (simplified)
            left = recent[0:10].max()
            head = recent[10:20].max()
            right = recent[20:30].max()
            
            if head > left and head > right and abs(left - right) / left < 0.05:
                self.patterns['Head and Shoulders'] = {
                    'detected': True,
                    'signal': 'Sell',
                    'confidence': 0.8
                }
                
    def get_trading_signal(self):
        """Get overall trading signal based on detected patterns"""
        buy_signals = 0
        sell_signals = 0
        
        for pattern, details in self.patterns.items():
            if details.get('detected', False):
                if details.get('signal') == 'Buy':
                    buy_signals += details.get('confidence', 0.5)
                elif details.get('signal') == 'Sell':
                    sell_signals += details.get('confidence', 0.5)
        
        if buy_signals > sell_signals:
            return "Buy", self.patterns
        elif sell_signals > buy_signals:
            return "Sell", self.patterns
        else:
            return "Hold", self.patterns
