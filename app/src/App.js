import MonsterPage from './components/MonsterPage';
import MonsterScrollBar from './components/MonsterScrollBar';
import SearchBar from './components/SearchBar';
import './index.css';

function App() {
  return (
    <div id="app-wrapper">
      <h1>Hello World</h1>
      <SearchBar/>
      <MonsterPage/>
      <MonsterScrollBar/>
    </div>
  );
}

export default App;
