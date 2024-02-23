import './index.css';
import MonsterPage from './components/MonsterPage/index.tsx';
import MonsterScrollBar from './components/MonsterScrollBar/index.tsx';
import SearchBar from './components/SearchBar/index.tsx';

function App() {
  return (
    <div id="app-wrapper">
      <h1>Hello World from App.tsx</h1>
      <SearchBar/>
      <MonsterPage/>
      <MonsterScrollBar/>
    </div>
  );
}

export default App;
